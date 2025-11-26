"""MCP Server implementation for World Professors Standard Library.

This module provides an MCP (Model Context Protocol) server that exposes
the standard library as queryable tools for AI assistants.
"""

import json
from pathlib import Path
from typing import Any

from world_professors.mcp.library import StandardLibrary


def create_server(data_dir: str = "data") -> "MCPServer":
    """Create and return an MCP server instance.

    Args:
        data_dir: Path to data directory

    Returns:
        Configured MCP server
    """
    return MCPServer(data_dir)


class MCPServer:
    """MCP Server for World Professors Standard Library.

    Exposes the following tools:
    - list_industries: List all industries
    - get_industry: Get industry details by ID
    - list_scenarios: List scenarios (optionally by industry)
    - get_scenario: Get scenario details by ID
    - list_workflows: List workflows (optionally by scenario)
    - get_workflow: Get workflow details by ID
    - list_agents: List agents (optionally by scenario/type)
    - get_agent: Get agent details by ID
    - get_agent_full_spec: Get agent with expanded capabilities/tools/workflows
    - list_tools: List tools (optionally by category)
    - get_tool: Get tool details by ID
    - list_capabilities: List capabilities (optionally by category)
    - get_capability: Get capability details by ID
    - get_scenario_overview: Get scenario with all related entities
    - search: Search across all entities
    - get_stats: Get library statistics
    """

    def __init__(self, data_dir: str = "data") -> None:
        """Initialize the MCP server."""
        self.library = StandardLibrary(Path(data_dir))
        self.tools = self._register_tools()

    def _register_tools(self) -> list[dict[str, Any]]:
        """Register all available tools."""
        return [
            {
                "name": "wp_list_industries",
                "description": "列出标准库中所有行业定义",
                "inputSchema": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
            {
                "name": "wp_get_industry",
                "description": "根据ID获取行业详细定义",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "industry_id": {
                            "type": "string",
                            "description": "行业ID，如 ind-finance, ind-technology",
                        },
                    },
                    "required": ["industry_id"],
                },
            },
            {
                "name": "wp_list_scenarios",
                "description": "列出场景定义，可按行业过滤",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "industry": {
                            "type": "string",
                            "description": "行业名称过滤（可选）",
                        },
                    },
                    "required": [],
                },
            },
            {
                "name": "wp_get_scenario",
                "description": "根据ID获取场景详细定义",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "scenario_id": {
                            "type": "string",
                            "description": "场景ID，如 scn-fin-wealth-mgmt",
                        },
                    },
                    "required": ["scenario_id"],
                },
            },
            {
                "name": "wp_list_workflows",
                "description": "列出工作流程定义，可按场景过滤",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "scenario_ref": {
                            "type": "string",
                            "description": "场景ID过滤（可选）",
                        },
                    },
                    "required": [],
                },
            },
            {
                "name": "wp_get_workflow",
                "description": "根据ID获取工作流程详细定义，包含所有步骤",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "workflow_id": {
                            "type": "string",
                            "description": "工作流程ID，如 wf-fin-wm-profiling",
                        },
                    },
                    "required": ["workflow_id"],
                },
            },
            {
                "name": "wp_list_agents",
                "description": "列出Agent定义，可按场景或类型过滤",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "scenario_ref": {
                            "type": "string",
                            "description": "场景ID过滤（可选）",
                        },
                        "agent_type": {
                            "type": "string",
                            "description": "Agent类型过滤：general/domain-expert/specialist/orchestrator",
                        },
                    },
                    "required": [],
                },
            },
            {
                "name": "wp_get_agent",
                "description": "根据ID获取Agent详细定义",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "agent_id": {
                            "type": "string",
                            "description": "Agent ID，如 agt-fin-wm-advisor",
                        },
                    },
                    "required": ["agent_id"],
                },
            },
            {
                "name": "wp_get_agent_full_spec",
                "description": "获取Agent完整规格，包含展开的能力、工具、流程定义",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "agent_id": {
                            "type": "string",
                            "description": "Agent ID",
                        },
                    },
                    "required": ["agent_id"],
                },
            },
            {
                "name": "wp_list_tools",
                "description": "列出工具定义，可按类别过滤",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "工具类别：data-retrieval/computation/generation/action",
                        },
                    },
                    "required": [],
                },
            },
            {
                "name": "wp_get_tool",
                "description": "根据ID获取工具详细定义，包含接口规范",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "tool_id": {
                            "type": "string",
                            "description": "工具ID，如 tool-code-generator",
                        },
                    },
                    "required": ["tool_id"],
                },
            },
            {
                "name": "wp_list_capabilities",
                "description": "列出能力定义，可按类别过滤",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "能力类别：cognitive/technical/interpersonal/domain-specific",
                        },
                    },
                    "required": [],
                },
            },
            {
                "name": "wp_get_capability",
                "description": "根据ID获取能力详细定义，包含等级和学习路径",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "capability_id": {
                            "type": "string",
                            "description": "能力ID，如 cap-tech-001",
                        },
                    },
                    "required": ["capability_id"],
                },
            },
            {
                "name": "wp_get_scenario_overview",
                "description": "获取场景完整概览，包含关联的工作流程和Agent",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "scenario_id": {
                            "type": "string",
                            "description": "场景ID",
                        },
                    },
                    "required": ["scenario_id"],
                },
            },
            {
                "name": "wp_search",
                "description": "搜索标准库，在名称和描述中查找匹配项",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "搜索关键词",
                        },
                        "entity_type": {
                            "type": "string",
                            "description": "实体类型过滤：industry/scenario/workflow/agent/tool/capability",
                        },
                    },
                    "required": ["query"],
                },
            },
            {
                "name": "wp_get_stats",
                "description": "获取标准库统计信息",
                "inputSchema": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
        ]

    def handle_tool_call(self, tool_name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        """Handle a tool call and return the result.

        Args:
            tool_name: Name of the tool to call
            arguments: Tool arguments

        Returns:
            Tool execution result
        """
        handlers = {
            "wp_list_industries": self._handle_list_industries,
            "wp_get_industry": self._handle_get_industry,
            "wp_list_scenarios": self._handle_list_scenarios,
            "wp_get_scenario": self._handle_get_scenario,
            "wp_list_workflows": self._handle_list_workflows,
            "wp_get_workflow": self._handle_get_workflow,
            "wp_list_agents": self._handle_list_agents,
            "wp_get_agent": self._handle_get_agent,
            "wp_get_agent_full_spec": self._handle_get_agent_full_spec,
            "wp_list_tools": self._handle_list_tools,
            "wp_get_tool": self._handle_get_tool,
            "wp_list_capabilities": self._handle_list_capabilities,
            "wp_get_capability": self._handle_get_capability,
            "wp_get_scenario_overview": self._handle_get_scenario_overview,
            "wp_search": self._handle_search,
            "wp_get_stats": self._handle_get_stats,
        }

        handler = handlers.get(tool_name)
        if not handler:
            return {"error": f"Unknown tool: {tool_name}"}

        try:
            return handler(arguments)
        except Exception as e:
            return {"error": str(e)}

    def _handle_list_industries(self, args: dict[str, Any]) -> dict[str, Any]:
        """Handle list_industries tool call."""
        industries = self.library.list_industries()
        return {"industries": industries, "count": len(industries)}

    def _handle_get_industry(self, args: dict[str, Any]) -> dict[str, Any]:
        """Handle get_industry tool call."""
        industry = self.library.get_industry(args["industry_id"])
        if not industry:
            return {"error": f"Industry not found: {args['industry_id']}"}
        return {
            "id": industry.id,
            "name": industry.name,
            "name_en": industry.name_en,
            "description": industry.description,
            "sub_industries": [
                {"id": s.id, "name": s.name} for s in industry.sub_industries
            ],
            "characteristics": industry.characteristics.model_dump() if industry.characteristics else None,
            "common_capabilities": industry.common_capabilities,
        }

    def _handle_list_scenarios(self, args: dict[str, Any]) -> dict[str, Any]:
        """Handle list_scenarios tool call."""
        scenarios = self.library.list_scenarios(args.get("industry"))
        return {"scenarios": scenarios, "count": len(scenarios)}

    def _handle_get_scenario(self, args: dict[str, Any]) -> dict[str, Any]:
        """Handle get_scenario tool call."""
        scenario = self.library.get_scenario(args["scenario_id"])
        if not scenario:
            return {"error": f"Scenario not found: {args['scenario_id']}"}
        return {
            "id": scenario.id,
            "name": scenario.name,
            "industry": scenario.industry,
            "description": scenario.description,
            "value_flow": [
                {"stage": v.stage, "activities": v.activities}
                for v in scenario.value_flow
            ],
            "key_metrics": scenario.key_metrics,
            "traditional_pain_points": scenario.traditional_pain_points,
            "ai_opportunities": scenario.ai_opportunities,
        }

    def _handle_list_workflows(self, args: dict[str, Any]) -> dict[str, Any]:
        """Handle list_workflows tool call."""
        workflows = self.library.list_workflows(args.get("scenario_ref"))
        return {"workflows": workflows, "count": len(workflows)}

    def _handle_get_workflow(self, args: dict[str, Any]) -> dict[str, Any]:
        """Handle get_workflow tool call."""
        workflow = self.library.get_workflow(args["workflow_id"])
        if not workflow:
            return {"error": f"Workflow not found: {args['workflow_id']}"}
        return {
            "id": workflow.id,
            "name": workflow.name,
            "scenario_ref": workflow.scenario_ref,
            "description": workflow.description,
            "steps": [
                {
                    "id": s.id,
                    "name": s.name,
                    "type": s.type.value,
                    "tools": s.tools,
                    "capabilities": s.capabilities,
                    "requires_human_confirmation": s.requires_human_confirmation,
                }
                for s in workflow.steps
            ],
            "human_checkpoints": workflow.human_checkpoints,
            "metrics": workflow.metrics.model_dump() if workflow.metrics else None,
            "automation_level": workflow.automation_level,
        }

    def _handle_list_agents(self, args: dict[str, Any]) -> dict[str, Any]:
        """Handle list_agents tool call."""
        agents = self.library.list_agents(
            args.get("scenario_ref"), args.get("agent_type")
        )
        return {"agents": agents, "count": len(agents)}

    def _handle_get_agent(self, args: dict[str, Any]) -> dict[str, Any]:
        """Handle get_agent tool call."""
        agent = self.library.get_agent(args["agent_id"])
        if not agent:
            return {"error": f"Agent not found: {args['agent_id']}"}
        return {
            "id": agent.id,
            "name": agent.name,
            "name_en": agent.name_en,
            "agent_type": agent.agent_type.value,
            "scenario_ref": agent.scenario_ref,
            "description": agent.description,
            "capabilities": {
                "required": [
                    {"id": c.id, "level": c.level.value} for c in agent.capabilities.required
                ],
                "optional": [
                    {"id": c.id, "level": c.level.value} for c in agent.capabilities.optional
                ],
            },
            "tools": [
                {"tool_ref": t.tool_ref, "usage": t.usage, "required": t.required}
                for t in agent.tools
            ],
            "executable_workflows": agent.executable_workflows,
            "constraints": {
                "compliance": agent.constraints.compliance,
                "boundaries": agent.constraints.boundaries,
                "escalation": [
                    {"condition": e.condition, "action": e.action}
                    for e in agent.constraints.escalation
                ],
            },
            "system_prompt": agent.system_prompt,
        }

    def _handle_get_agent_full_spec(self, args: dict[str, Any]) -> dict[str, Any]:
        """Handle get_agent_full_spec tool call."""
        spec = self.library.get_agent_full_spec(args["agent_id"])
        if not spec:
            return {"error": f"Agent not found: {args['agent_id']}"}
        return spec

    def _handle_list_tools(self, args: dict[str, Any]) -> dict[str, Any]:
        """Handle list_tools tool call."""
        tools = self.library.list_tools(args.get("category"))
        return {"tools": tools, "count": len(tools)}

    def _handle_get_tool(self, args: dict[str, Any]) -> dict[str, Any]:
        """Handle get_tool tool call."""
        tool = self.library.get_tool(args["tool_id"])
        if not tool:
            return {"error": f"Tool not found: {args['tool_id']}"}
        return {
            "id": tool.id,
            "name": tool.name,
            "name_en": tool.name_en,
            "category": tool.category.value,
            "description": tool.description,
            "interface": {
                "type": tool.interface.type.value,
                "endpoints": [
                    {"name": e.name, "method": e.method, "path": e.path}
                    for e in tool.interface.endpoints
                ],
            },
            "requirements": {
                "auth_type": tool.requirements.authentication.type.value
                if tool.requirements and tool.requirements.authentication
                else None,
                "rate_limit": tool.requirements.rate_limit.model_dump()
                if tool.requirements and tool.requirements.rate_limit
                else None,
            },
            "pricing": tool.pricing.model_dump() if tool.pricing else None,
            "providers": [{"name": p.name, "tier": p.tier} for p in tool.providers],
        }

    def _handle_list_capabilities(self, args: dict[str, Any]) -> dict[str, Any]:
        """Handle list_capabilities tool call."""
        capabilities = self.library.list_capabilities(args.get("category"))
        return {"capabilities": capabilities, "count": len(capabilities)}

    def _handle_get_capability(self, args: dict[str, Any]) -> dict[str, Any]:
        """Handle get_capability tool call."""
        cap = self.library.get_capability(args["capability_id"])
        if not cap:
            return {"error": f"Capability not found: {args['capability_id']}"}
        return {
            "id": cap.id,
            "name": cap.name,
            "name_en": cap.name_en,
            "category": cap.category.value,
            "description": cap.description,
            "levels": {
                name: {
                    "description": level.description,
                    "skills": level.skills,
                    "tasks": level.tasks,
                }
                for name, level in cap.levels.items()
            },
            "learning_path": {
                "prerequisites": cap.learning_path.prerequisites,
                "estimated_time": cap.learning_path.estimated_time,
                "milestones": [
                    {"month": m.month, "goal": m.goal}
                    for m in cap.learning_path.milestones
                ],
            }
            if cap.learning_path
            else None,
            "transferability": cap.transferability.model_dump() if cap.transferability else None,
            "ai_impact": cap.ai_impact.value if cap.ai_impact else None,
        }

    def _handle_get_scenario_overview(self, args: dict[str, Any]) -> dict[str, Any]:
        """Handle get_scenario_overview tool call."""
        overview = self.library.get_scenario_overview(args["scenario_id"])
        if not overview:
            return {"error": f"Scenario not found: {args['scenario_id']}"}
        return overview

    def _handle_search(self, args: dict[str, Any]) -> dict[str, Any]:
        """Handle search tool call."""
        results = self.library.search(args["query"], args.get("entity_type"))
        return {"results": results, "count": len(results)}

    def _handle_get_stats(self, args: dict[str, Any]) -> dict[str, Any]:
        """Handle get_stats tool call."""
        return self.library.get_stats()

    def get_tools_schema(self) -> list[dict[str, Any]]:
        """Get the schema for all registered tools."""
        return self.tools

    def to_json(self) -> str:
        """Export tools schema as JSON."""
        return json.dumps(self.tools, indent=2, ensure_ascii=False)
