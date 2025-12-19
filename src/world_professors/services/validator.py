"""Data validation service (schema + reference + quality gates)."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

import yaml

from world_professors.models import Agent, Capability, Industry, Role, Scenario, Tool, Workflow
from world_professors.repositories import RepositoryFactory


@dataclass(frozen=True)
class ValidationMessage:
    """A validation message with severity."""

    severity: str  # "error" | "warning"
    file_path: Path
    code: str
    message: str


@dataclass
class ValidationSummary:
    """Validation summary for a run."""

    checked_files: int = 0
    errors: list[ValidationMessage] = field(default_factory=list)
    warnings: list[ValidationMessage] = field(default_factory=list)

    def add(self, msg: ValidationMessage) -> None:
        if msg.severity == "error":
            self.errors.append(msg)
        else:
            self.warnings.append(msg)

    @property
    def ok(self) -> bool:
        return len(self.errors) == 0


class DataValidator:
    """Validate repository data directory."""

    def __init__(self, data_dir: Path) -> None:
        self.data_dir = Path(data_dir)
        self.repos = RepositoryFactory(self.data_dir)

    def iter_yaml_files(self) -> Iterable[Path]:
        """Iterate all YAML files under data_dir, excluding templates/catalog."""
        if not self.data_dir.exists():
            return []

        excluded_parts = {"templates", "_catalog", ".git", "__pycache__"}
        out: list[Path] = []
        for p in self.data_dir.rglob("*.yaml"):
            if any(part in excluded_parts for part in p.parts):
                continue
            out.append(p)
        return out

    def classify_model(self, file_path: Path) -> type[Any] | None:
        """Classify a YAML file into a model based on its path."""
        parts = set(file_path.parts)
        if "industries" in parts:
            return Industry
        if "scenarios" in parts:
            return Scenario
        if "workflows" in parts:
            return Workflow
        if "agents" in parts:
            return Agent
        if "tools" in parts:
            return Tool
        if "capabilities" in parts:
            return Capability
        if "roles" in parts:
            return Role
        return None

    def validate(
        self,
        *,
        strict_refs: bool = False,
        strict_quality: bool = False,
    ) -> ValidationSummary:
        """Validate all YAML files in the data directory.

        Args:
            strict_refs: If True, missing references are errors; otherwise warnings.
            strict_quality: If True, quality gate violations are errors; otherwise warnings.
        """
        summary = ValidationSummary()

        # Load all entities first (best-effort) so reference checks can use indices.
        # These calls are resilient because BaseRepository skips invalid files during indexing.
        _ = (
            self.repos.industries.load_all()
            + self.repos.scenarios.load_all()
            + self.repos.workflows.load_all()
            + self.repos.agents.load_all()
            + self.repos.tools.load_all()
            + self.repos.capabilities.load_all()
        )

        for file_path in self.iter_yaml_files():
            model = self.classify_model(file_path)
            if model is None:
                continue

            summary.checked_files += 1
            try:
                with open(file_path, encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                entity = model.model_validate(data)
            except Exception as e:  # noqa: BLE001 - want full capture
                summary.add(
                    ValidationMessage(
                        severity="error",
                        file_path=file_path,
                        code="schema.invalid",
                        message=str(e),
                    )
                )
                continue

            # Reference + quality checks (best-effort per entity type)
            if isinstance(entity, Scenario):
                self._check_scenario(entity, file_path, summary, strict_refs, strict_quality)
            elif isinstance(entity, Workflow):
                self._check_workflow(entity, file_path, summary, strict_refs, strict_quality)
            elif isinstance(entity, Agent):
                self._check_agent(entity, file_path, summary, strict_refs, strict_quality)
            elif isinstance(entity, Tool):
                self._check_tool(entity, file_path, summary, strict_refs)
            elif isinstance(entity, Capability):
                self._check_capability(entity, file_path, summary, strict_refs)
            elif isinstance(entity, Industry):
                self._check_industry(entity, file_path, summary, strict_refs)

        return summary

    def _emit(
        self,
        summary: ValidationSummary,
        *,
        strict: bool,
        file_path: Path,
        code: str,
        message: str,
    ) -> None:
        summary.add(
            ValidationMessage(
                severity="error" if strict else "warning",
                file_path=file_path,
                code=code,
                message=message,
            )
        )

    def _check_scenario(
        self,
        scenario: Scenario,
        file_path: Path,
        summary: ValidationSummary,
        strict_refs: bool,
        strict_quality: bool,
    ) -> None:
        # related_scenarios existence
        for related_id in scenario.related_scenarios:
            if not self.repos.scenarios.exists(related_id):
                self._emit(
                    summary,
                    strict=strict_refs,
                    file_path=file_path,
                    code="ref.scenario.missing",
                    message=f"related_scenarios 引用不存在: {related_id}",
                )

        # quality gates (configurable)
        if len(scenario.value_flow) < 3:
            self._emit(
                summary,
                strict=strict_quality,
                file_path=file_path,
                code="quality.scenario.value_flow.too_small",
                message="value_flow 建议至少 3 个阶段",
            )
        for stage in scenario.value_flow:
            if len(stage.activities) < 3:
                self._emit(
                    summary,
                    strict=strict_quality,
                    file_path=file_path,
                    code="quality.scenario.activities.too_small",
                    message=f"value_flow 阶段 '{stage.stage}' 的 activities 建议至少 3 条",
                )
        if len(scenario.ai_opportunities) < 5:
            self._emit(
                summary,
                strict=strict_quality,
                file_path=file_path,
                code="quality.scenario.ai_opportunities.too_small",
                message="ai_opportunities 建议至少 5 条",
            )
        if len(scenario.tags) < 3:
            self._emit(
                summary,
                strict=strict_quality,
                file_path=file_path,
                code="quality.scenario.tags.too_small",
                message="tags 建议至少 3 个",
            )

    def _check_workflow(
        self,
        workflow: Workflow,
        file_path: Path,
        summary: ValidationSummary,
        strict_refs: bool,
        strict_quality: bool,
    ) -> None:
        if not self.repos.scenarios.exists(workflow.scenario_ref):
            self._emit(
                summary,
                strict=strict_refs,
                file_path=file_path,
                code="ref.workflow.scenario_missing",
                message=f"scenario_ref 引用不存在: {workflow.scenario_ref}",
            )

        step_ids = set(workflow.step_ids)
        # depends_on validity
        for step in workflow.steps:
            for dep in step.depends_on:
                if dep not in step_ids:
                    self._emit(
                        summary,
                        strict=strict_refs,
                        file_path=file_path,
                        code="ref.workflow.depends_on_missing",
                        message=f"{step.id} depends_on 引用不存在: {dep}",
                    )

        # tool/cap references
        for step in workflow.steps:
            for tool_id in step.tools:
                if not self.repos.tools.exists(tool_id):
                    self._emit(
                        summary,
                        strict=strict_refs,
                        file_path=file_path,
                        code="ref.workflow.tool_missing",
                        message=f"{step.id} tools 引用不存在: {tool_id}",
                    )
            for cap_id in step.capabilities:
                if not self.repos.capabilities.exists(cap_id):
                    self._emit(
                        summary,
                        strict=strict_refs,
                        file_path=file_path,
                        code="ref.workflow.capability_missing",
                        message=f"{step.id} capabilities 引用不存在: {cap_id}",
                    )

        # human checkpoints validity
        for checkpoint in workflow.human_checkpoints:
            if checkpoint not in step_ids:
                self._emit(
                    summary,
                    strict=strict_refs,
                    file_path=file_path,
                    code="ref.workflow.human_checkpoint_missing",
                    message=f"human_checkpoints 引用不存在: {checkpoint}",
                )

        # quality
        if len(workflow.steps) < 4:
            self._emit(
                summary,
                strict=strict_quality,
                file_path=file_path,
                code="quality.workflow.steps.too_small",
                message="steps 建议至少 4 个",
            )

    def _check_agent(
        self,
        agent: Agent,
        file_path: Path,
        summary: ValidationSummary,
        strict_refs: bool,
        strict_quality: bool,
    ) -> None:
        if not self.repos.scenarios.exists(agent.scenario_ref):
            self._emit(
                summary,
                strict=strict_refs,
                file_path=file_path,
                code="ref.agent.scenario_missing",
                message=f"scenario_ref 引用不存在: {agent.scenario_ref}",
            )

        for wf_id in agent.executable_workflows:
            if not self.repos.workflows.exists(wf_id):
                self._emit(
                    summary,
                    strict=strict_refs,
                    file_path=file_path,
                    code="ref.agent.workflow_missing",
                    message=f"executable_workflows 引用不存在: {wf_id}",
                )

        for tool_ref in agent.all_tool_ids:
            if not self.repos.tools.exists(tool_ref):
                self._emit(
                    summary,
                    strict=strict_refs,
                    file_path=file_path,
                    code="ref.agent.tool_missing",
                    message=f"tools 引用不存在: {tool_ref}",
                )

        for cap_id in agent.all_capability_ids:
            if not self.repos.capabilities.exists(cap_id):
                self._emit(
                    summary,
                    strict=strict_refs,
                    file_path=file_path,
                    code="ref.agent.capability_missing",
                    message=f"capabilities 引用不存在: {cap_id}",
                )

        # quality: constraints basics
        if len(agent.constraints.compliance) < 1:
            self._emit(
                summary,
                strict=strict_quality,
                file_path=file_path,
                code="quality.agent.compliance.empty",
                message="constraints.compliance 建议至少 1 条",
            )
        if len(agent.constraints.boundaries) < 1:
            self._emit(
                summary,
                strict=strict_quality,
                file_path=file_path,
                code="quality.agent.boundaries.empty",
                message="constraints.boundaries 建议至少 1 条",
            )

    def _check_tool(
        self, tool: Tool, file_path: Path, summary: ValidationSummary, strict_refs: bool
    ) -> None:
        for ind_id in tool.applicable_industries:
            if not self.repos.industries.exists(ind_id):
                self._emit(
                    summary,
                    strict=strict_refs,
                    file_path=file_path,
                    code="ref.tool.industry_missing",
                    message=f"applicable_industries 引用不存在: {ind_id}",
                )
        for scn_id in tool.applicable_scenarios:
            if not self.repos.scenarios.exists(scn_id):
                self._emit(
                    summary,
                    strict=strict_refs,
                    file_path=file_path,
                    code="ref.tool.scenario_missing",
                    message=f"applicable_scenarios 引用不存在: {scn_id}",
                )
        for cap_id in tool.related_capabilities:
            if not self.repos.capabilities.exists(cap_id):
                self._emit(
                    summary,
                    strict=strict_refs,
                    file_path=file_path,
                    code="ref.tool.capability_missing",
                    message=f"related_capabilities 引用不存在: {cap_id}",
                )

    def _check_capability(
        self, cap: Capability, file_path: Path, summary: ValidationSummary, strict_refs: bool
    ) -> None:
        for related_id in cap.related_capabilities:
            if not self.repos.capabilities.exists(related_id):
                self._emit(
                    summary,
                    strict=strict_refs,
                    file_path=file_path,
                    code="ref.capability.related_missing",
                    message=f"related_capabilities 引用不存在: {related_id}",
                )
        if cap.learning_path is not None:
            for prereq_id in cap.learning_path.prerequisites:
                if not self.repos.capabilities.exists(prereq_id):
                    self._emit(
                        summary,
                        strict=strict_refs,
                        file_path=file_path,
                        code="ref.capability.prereq_missing",
                        message=f"learning_path.prerequisites 引用不存在: {prereq_id}",
                    )

    def _check_industry(
        self, industry: Industry, file_path: Path, summary: ValidationSummary, strict_refs: bool
    ) -> None:
        for related_id in industry.related_industries:
            if not self.repos.industries.exists(related_id):
                self._emit(
                    summary,
                    strict=strict_refs,
                    file_path=file_path,
                    code="ref.industry.related_missing",
                    message=f"related_industries 引用不存在: {related_id}",
                )
        for cap_id in industry.common_capabilities:
            if not self.repos.capabilities.exists(cap_id):
                self._emit(
                    summary,
                    strict=strict_refs,
                    file_path=file_path,
                    code="ref.industry.capability_missing",
                    message=f"common_capabilities 引用不存在: {cap_id}",
                )

