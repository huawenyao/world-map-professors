"""Catalog builder for data navigation and analysis."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from world_professors.repositories import RepositoryFactory
from world_professors.services.validator import DataValidator


@dataclass(frozen=True)
class CatalogPaths:
    root: Path

    @property
    def entities(self) -> Path:
        return self.root / "entities.json"

    @property
    def links(self) -> Path:
        return self.root / "links.json"

    @property
    def stats(self) -> Path:
        return self.root / "stats.json"


class CatalogBuilder:
    """Build `_catalog` artifacts under data directory."""

    def __init__(self, data_dir: Path) -> None:
        self.data_dir = Path(data_dir)
        self.repos = RepositoryFactory(self.data_dir)
        self.validator = DataValidator(self.data_dir)

    def build(self, *, output_dir: Path | None = None) -> CatalogPaths:
        out_root = Path(output_dir) if output_dir is not None else (self.data_dir / "_catalog")
        out_root.mkdir(parents=True, exist_ok=True)
        paths = CatalogPaths(root=out_root)

        entities: dict[str, dict[str, Any]] = {}
        links: list[dict[str, Any]] = []

        def add_entity(entity_type: str, repo: Any) -> None:
            for entity_id in repo.iter_ids():
                try:
                    p = repo.get_path(entity_id)
                except Exception:
                    continue
                entities[entity_id] = {
                    "type": entity_type,
                    "path": str(p.relative_to(self.data_dir)),
                }

        # Index entities
        add_entity("industry", self.repos.industries)
        add_entity("scenario", self.repos.scenarios)
        add_entity("workflow", self.repos.workflows)
        add_entity("agent", self.repos.agents)
        add_entity("tool", self.repos.tools)
        add_entity("capability", self.repos.capabilities)
        add_entity("role", self.repos.roles)

        # Build links (best-effort)
        for scn in self.repos.scenarios.load_all():
            for rid in scn.related_scenarios:
                links.append({"from": scn.id, "to": rid, "kind": "scenario.related"})

        for wf in self.repos.workflows.load_all():
            links.append({"from": wf.id, "to": wf.scenario_ref, "kind": "workflow.scenario_ref"})
            for step in wf.steps:
                for tool_id in step.tools:
                    links.append(
                        {
                            "from": wf.id,
                            "to": tool_id,
                            "kind": "workflow.step.tool",
                            "step_id": step.id,
                        }
                    )
                for cap_id in step.capabilities:
                    links.append(
                        {
                            "from": wf.id,
                            "to": cap_id,
                            "kind": "workflow.step.capability",
                            "step_id": step.id,
                        }
                    )

        for agt in self.repos.agents.load_all():
            links.append({"from": agt.id, "to": agt.scenario_ref, "kind": "agent.scenario_ref"})
            for wf_id in agt.executable_workflows:
                links.append({"from": agt.id, "to": wf_id, "kind": "agent.workflow"})
            for tool_id in agt.all_tool_ids:
                links.append({"from": agt.id, "to": tool_id, "kind": "agent.tool"})
            for cap_id in agt.all_capability_ids:
                links.append({"from": agt.id, "to": cap_id, "kind": "agent.capability"})

        for tool in self.repos.tools.load_all():
            for ind_id in tool.applicable_industries:
                links.append({"from": tool.id, "to": ind_id, "kind": "tool.applicable_industry"})
            for scn_id in tool.applicable_scenarios:
                links.append({"from": tool.id, "to": scn_id, "kind": "tool.applicable_scenario"})
            for cap_id in tool.related_capabilities:
                links.append({"from": tool.id, "to": cap_id, "kind": "tool.related_capability"})

        for cap in self.repos.capabilities.load_all():
            for rid in cap.related_capabilities:
                links.append({"from": cap.id, "to": rid, "kind": "capability.related"})
            if cap.learning_path is not None:
                for pid in cap.learning_path.prerequisites:
                    links.append({"from": cap.id, "to": pid, "kind": "capability.prerequisite"})

        for ind in self.repos.industries.load_all():
            for rid in ind.related_industries:
                links.append({"from": ind.id, "to": rid, "kind": "industry.related"})
            for cap_id in ind.common_capabilities:
                links.append({"from": ind.id, "to": cap_id, "kind": "industry.common_capability"})

        # Stats from validator (non-strict by default)
        validation = self.validator.validate(strict_refs=False, strict_quality=False)
        stats = {
            "counts": {
                "industries": self.repos.industries.count(),
                "scenarios": self.repos.scenarios.count(),
                "workflows": self.repos.workflows.count(),
                "agents": self.repos.agents.count(),
                "tools": self.repos.tools.count(),
                "capabilities": self.repos.capabilities.count(),
                "roles": self.repos.roles.count(),
            },
            "validation": {
                "checked_files": validation.checked_files,
                "errors": len(validation.errors),
                "warnings": len(validation.warnings),
            },
        }

        paths.entities.write_text(json.dumps(entities, ensure_ascii=False, indent=2), encoding="utf-8")
        paths.links.write_text(json.dumps(links, ensure_ascii=False, indent=2), encoding="utf-8")
        paths.stats.write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")

        return paths

