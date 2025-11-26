"""Standard Library API for querying entities."""

from pathlib import Path
from typing import Any

import yaml

from world_professors.models import (
    Agent,
    Capability,
    Industry,
    Scenario,
    Tool,
    Workflow,
)


class StandardLibrary:
    """Standard Library for querying industry agent definitions.

    Provides a unified interface to query all entity types:
    - Industry, Scenario, Workflow, Agent, Tool, Capability
    """

    def __init__(self, data_dir: Path | str = "data") -> None:
        """Initialize the standard library.

        Args:
            data_dir: Root directory containing all data files
        """
        self.data_dir = Path(data_dir)
        self._cache: dict[str, dict[str, Any]] = {
            "industries": {},
            "scenarios": {},
            "workflows": {},
            "agents": {},
            "tools": {},
            "capabilities": {},
        }
        self._load_all()

    def _load_all(self) -> None:
        """Load all entities from data directory."""
        self._load_industries()
        self._load_scenarios()
        self._load_workflows()
        self._load_agents()
        self._load_tools()
        self._load_capabilities()

    def _load_yaml(self, file_path: Path) -> dict[str, Any]:
        """Load and parse YAML file."""
        with open(file_path, encoding="utf-8") as f:
            return yaml.safe_load(f)

    def _load_industries(self) -> None:
        """Load all industry definitions."""
        industries_dir = self.data_dir / "industries"
        if not industries_dir.exists():
            return
        for yaml_file in industries_dir.glob("*.yaml"):
            try:
                data = self._load_yaml(yaml_file)
                industry = Industry(**data)
                self._cache["industries"][industry.id] = industry
            except Exception:
                continue

    def _load_scenarios(self) -> None:
        """Load all scenario definitions."""
        scenarios_dir = self.data_dir / "scenarios"
        if not scenarios_dir.exists():
            return
        for yaml_file in scenarios_dir.rglob("*.yaml"):
            try:
                data = self._load_yaml(yaml_file)
                scenario = Scenario(**data)
                self._cache["scenarios"][scenario.id] = scenario
            except Exception:
                continue

    def _load_workflows(self) -> None:
        """Load all workflow definitions."""
        workflows_dir = self.data_dir / "workflows"
        if not workflows_dir.exists():
            return
        for yaml_file in workflows_dir.rglob("*.yaml"):
            try:
                data = self._load_yaml(yaml_file)
                workflow = Workflow(**data)
                self._cache["workflows"][workflow.id] = workflow
            except Exception:
                continue

    def _load_agents(self) -> None:
        """Load all agent definitions."""
        agents_dir = self.data_dir / "agents"
        if not agents_dir.exists():
            return
        for yaml_file in agents_dir.rglob("*.yaml"):
            try:
                data = self._load_yaml(yaml_file)
                agent = Agent(**data)
                self._cache["agents"][agent.id] = agent
            except Exception:
                continue

    def _load_tools(self) -> None:
        """Load all tool definitions."""
        tools_dir = self.data_dir / "tools"
        if not tools_dir.exists():
            return
        for yaml_file in tools_dir.rglob("*.yaml"):
            try:
                data = self._load_yaml(yaml_file)
                tool = Tool(**data)
                self._cache["tools"][tool.id] = tool
            except Exception:
                continue

    def _load_capabilities(self) -> None:
        """Load all capability definitions."""
        capabilities_dir = self.data_dir / "capabilities"
        if not capabilities_dir.exists():
            return
        for yaml_file in capabilities_dir.rglob("*.yaml"):
            try:
                data = self._load_yaml(yaml_file)
                capability = Capability(**data)
                self._cache["capabilities"][capability.id] = capability
            except Exception:
                continue

    # === Query Methods ===

    def list_industries(self) -> list[dict[str, Any]]:
        """List all industries."""
        return [
            {"id": ind.id, "name": ind.name, "name_en": ind.name_en}
            for ind in self._cache["industries"].values()
        ]

    def get_industry(self, industry_id: str) -> Industry | None:
        """Get industry by ID."""
        return self._cache["industries"].get(industry_id)

    def list_scenarios(self, industry: str | None = None) -> list[dict[str, Any]]:
        """List all scenarios, optionally filtered by industry."""
        scenarios = self._cache["scenarios"].values()
        if industry:
            scenarios = [s for s in scenarios if industry.lower() in s.industry.lower()]
        return [
            {"id": s.id, "name": s.name, "industry": s.industry}
            for s in scenarios
        ]

    def get_scenario(self, scenario_id: str) -> Scenario | None:
        """Get scenario by ID."""
        return self._cache["scenarios"].get(scenario_id)

    def list_workflows(self, scenario_ref: str | None = None) -> list[dict[str, Any]]:
        """List all workflows, optionally filtered by scenario."""
        workflows = self._cache["workflows"].values()
        if scenario_ref:
            workflows = [w for w in workflows if w.scenario_ref == scenario_ref]
        return [
            {
                "id": w.id,
                "name": w.name,
                "scenario_ref": w.scenario_ref,
                "steps_count": len(w.steps),
            }
            for w in workflows
        ]

    def get_workflow(self, workflow_id: str) -> Workflow | None:
        """Get workflow by ID."""
        return self._cache["workflows"].get(workflow_id)

    def list_agents(
        self, scenario_ref: str | None = None, agent_type: str | None = None
    ) -> list[dict[str, Any]]:
        """List all agents, optionally filtered by scenario or type."""
        agents = list(self._cache["agents"].values())
        if scenario_ref:
            agents = [a for a in agents if a.scenario_ref == scenario_ref]
        if agent_type:
            agents = [a for a in agents if a.agent_type.value == agent_type]
        return [
            {
                "id": a.id,
                "name": a.name,
                "agent_type": a.agent_type.value,
                "scenario_ref": a.scenario_ref,
            }
            for a in agents
        ]

    def get_agent(self, agent_id: str) -> Agent | None:
        """Get agent by ID."""
        return self._cache["agents"].get(agent_id)

    def list_tools(self, category: str | None = None) -> list[dict[str, Any]]:
        """List all tools, optionally filtered by category."""
        tools = list(self._cache["tools"].values())
        if category:
            tools = [t for t in tools if t.category.value == category]
        return [
            {"id": t.id, "name": t.name, "category": t.category.value}
            for t in tools
        ]

    def get_tool(self, tool_id: str) -> Tool | None:
        """Get tool by ID."""
        return self._cache["tools"].get(tool_id)

    def list_capabilities(self, category: str | None = None) -> list[dict[str, Any]]:
        """List all capabilities, optionally filtered by category."""
        capabilities = list(self._cache["capabilities"].values())
        if category:
            capabilities = [c for c in capabilities if c.category.value == category]
        return [
            {"id": c.id, "name": c.name, "category": c.category.value}
            for c in capabilities
        ]

    def get_capability(self, capability_id: str) -> Capability | None:
        """Get capability by ID."""
        return self._cache["capabilities"].get(capability_id)

    # === Composite Queries ===

    def get_agent_full_spec(self, agent_id: str) -> dict[str, Any] | None:
        """Get full agent specification including related entities.

        Returns agent with expanded:
        - Capabilities (full definitions)
        - Tools (full definitions)
        - Workflows (full definitions)
        """
        agent = self.get_agent(agent_id)
        if not agent:
            return None

        # Get related capabilities
        capabilities = []
        for cap_req in agent.capabilities.required:
            cap = self.get_capability(cap_req.id)
            if cap:
                capabilities.append({
                    "id": cap.id,
                    "name": cap.name,
                    "level": cap_req.level.value,
                    "category": cap.category.value,
                })

        # Get related tools
        tools = []
        for tool_ref in agent.tools:
            tool = self.get_tool(tool_ref.tool_ref)
            if tool:
                tools.append({
                    "id": tool.id,
                    "name": tool.name,
                    "category": tool.category.value,
                    "usage": tool_ref.usage,
                    "required": tool_ref.required,
                })

        # Get related workflows
        workflows = []
        for wf_id in agent.executable_workflows:
            wf = self.get_workflow(wf_id)
            if wf:
                workflows.append({
                    "id": wf.id,
                    "name": wf.name,
                    "steps_count": len(wf.steps),
                })

        return {
            "agent": {
                "id": agent.id,
                "name": agent.name,
                "name_en": agent.name_en,
                "agent_type": agent.agent_type.value,
                "scenario_ref": agent.scenario_ref,
                "description": agent.description,
            },
            "capabilities": capabilities,
            "tools": tools,
            "workflows": workflows,
            "constraints": {
                "compliance": agent.constraints.compliance,
                "boundaries": agent.constraints.boundaries,
                "escalation_rules": len(agent.constraints.escalation),
            },
        }

    def get_scenario_overview(self, scenario_id: str) -> dict[str, Any] | None:
        """Get scenario overview with all related entities."""
        scenario = self.get_scenario(scenario_id)
        if not scenario:
            return None

        # Get workflows for this scenario
        workflows = self.list_workflows(scenario_ref=scenario_id)

        # Get agents for this scenario
        agents = self.list_agents(scenario_ref=scenario_id)

        return {
            "scenario": {
                "id": scenario.id,
                "name": scenario.name,
                "industry": scenario.industry,
                "description": scenario.description,
            },
            "value_flow": [
                {"stage": v.stage, "activities": v.activities}
                for v in scenario.value_flow
            ],
            "workflows": workflows,
            "agents": agents,
            "ai_opportunities": scenario.ai_opportunities,
        }

    def search(self, query: str, entity_type: str | None = None) -> list[dict[str, Any]]:
        """Search across all entities by name or description.

        Args:
            query: Search query string
            entity_type: Optional filter by type (industry/scenario/workflow/agent/tool/capability)
        """
        results = []
        query_lower = query.lower()

        entity_types = (
            [entity_type] if entity_type else
            ["industries", "scenarios", "workflows", "agents", "tools", "capabilities"]
        )

        for et in entity_types:
            if et == "industries":
                et = "industries"
            elif et == "industry":
                et = "industries"
            elif et == "scenario":
                et = "scenarios"
            elif et == "workflow":
                et = "workflows"
            elif et == "agent":
                et = "agents"
            elif et == "tool":
                et = "tools"
            elif et == "capability":
                et = "capabilities"

            for entity in self._cache.get(et, {}).values():
                if (
                    query_lower in entity.name.lower()
                    or query_lower in entity.description.lower()
                    or (hasattr(entity, "name_en") and entity.name_en and query_lower in entity.name_en.lower())
                ):
                    results.append({
                        "type": et.rstrip("s"),
                        "id": entity.id,
                        "name": entity.name,
                        "description": entity.description[:100] + "..."
                        if len(entity.description) > 100
                        else entity.description,
                    })

        return results

    def get_stats(self) -> dict[str, int]:
        """Get statistics about the library."""
        return {
            "industries": len(self._cache["industries"]),
            "scenarios": len(self._cache["scenarios"]),
            "workflows": len(self._cache["workflows"]),
            "agents": len(self._cache["agents"]),
            "tools": len(self._cache["tools"]),
            "capabilities": len(self._cache["capabilities"]),
        }
