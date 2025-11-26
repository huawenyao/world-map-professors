"""Agent model for AI agents in industry scenarios."""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, field_validator

from world_professors.models.base import BaseEntity
from world_professors.models.role import CapabilityLevel


class AgentType(str, Enum):
    """Agent type classification."""

    GENERAL = "general"
    DOMAIN_EXPERT = "domain-expert"
    SPECIALIST = "specialist"
    ORCHESTRATOR = "orchestrator"
    ASSISTANT = "assistant"


class RequiredCapability(BaseModel):
    """Capability requirement for an agent."""

    id: str = Field(..., pattern=r"^cap-[a-z]+-\d{3}$")
    level: CapabilityLevel = CapabilityLevel.INTERMEDIATE
    description: str | None = None


class AgentCapabilities(BaseModel):
    """Agent capability requirements."""

    required: list[RequiredCapability] = Field(
        default_factory=list,
        description="Capabilities that agent must have",
    )
    optional: list[RequiredCapability] = Field(
        default_factory=list,
        description="Optional capabilities for enhancement",
    )


class ToolReference(BaseModel):
    """Reference to a tool used by agent."""

    tool_ref: str = Field(..., description="Tool ID reference")
    usage: str | None = Field(None, description="How agent uses this tool")
    required: bool = True


class InterfaceSchema(BaseModel):
    """Input/Output schema for agent interface."""

    type: str = "object"
    properties: dict[str, Any] = Field(default_factory=dict)
    required: list[str] = Field(default_factory=list)


class AgentInterface(BaseModel):
    """Agent input/output interface specification."""

    input_schema: InterfaceSchema = Field(default_factory=InterfaceSchema)
    output_schema: InterfaceSchema = Field(default_factory=InterfaceSchema)


class EscalationRule(BaseModel):
    """Rule for when to escalate to human."""

    condition: str = Field(..., description="Condition that triggers escalation")
    action: str = Field(
        ...,
        description="Action to take: transfer_to_human, request_review, require_approval",
    )
    priority: str = Field(default="normal", description="low, normal, high, critical")


class AgentConstraints(BaseModel):
    """Constraints and boundaries for agent behavior."""

    # Compliance rules
    compliance: list[str] = Field(
        default_factory=list,
        description="Compliance rules agent must follow",
    )

    # Capability boundaries
    boundaries: list[str] = Field(
        default_factory=list,
        description="Things agent cannot do",
    )

    # Escalation conditions
    escalation: list[EscalationRule] = Field(
        default_factory=list,
        description="When to escalate to human",
    )


class QualityMetric(BaseModel):
    """Quality metric definition."""

    name: str = Field(..., min_length=1)
    target: str = Field(..., description="Target value, e.g., '>= 90%'")
    measurement: str | None = None


class EfficiencyMetric(BaseModel):
    """Efficiency metric definition."""

    name: str = Field(..., min_length=1)
    target: str = Field(..., description="Target value, e.g., '< 3s'")


class AgentMetrics(BaseModel):
    """Agent performance metrics."""

    quality: list[QualityMetric] = Field(default_factory=list)
    efficiency: list[EfficiencyMetric] = Field(default_factory=list)


class Agent(BaseEntity):
    """Agent definition model.

    Represents a complete AI agent specification including:
    - Capabilities it needs
    - Tools it uses
    - Workflows it can execute
    - Interface specification
    - Behavioral constraints
    """

    # Naming
    name_en: str | None = Field(None, description="English name")

    # Classification
    agent_type: AgentType = Field(
        default=AgentType.DOMAIN_EXPERT,
        description="Type of agent",
    )

    # Reference
    scenario_ref: str = Field(..., description="Reference to scenario ID")

    # Capabilities
    capabilities: AgentCapabilities = Field(
        default_factory=AgentCapabilities,
        description="Required and optional capabilities",
    )

    # Tools
    tools: list[ToolReference] = Field(
        default_factory=list,
        description="Tools agent can use",
    )

    # Executable workflows
    executable_workflows: list[str] = Field(
        default_factory=list,
        description="Workflow IDs this agent can execute",
    )

    # Interface
    interface: AgentInterface = Field(
        default_factory=AgentInterface,
        description="Input/output interface specification",
    )

    # Constraints
    constraints: AgentConstraints = Field(
        default_factory=AgentConstraints,
        description="Behavioral constraints and escalation rules",
    )

    # Metrics
    metrics: AgentMetrics | None = None

    # Prompt template (optional, for LLM-based agents)
    system_prompt: str | None = Field(
        None,
        description="System prompt template for LLM-based agents",
    )

    @field_validator("id")
    @classmethod
    def validate_agent_id(cls, v: str) -> str:
        """Validate agent ID format: agt-{industry}-{scenario}-{name}."""
        if not v.startswith("agt-"):
            raise ValueError(f"Agent ID must start with 'agt-': {v}")
        parts = v.split("-")
        if len(parts) < 4:
            raise ValueError(
                f"Agent ID format error: {v}, "
                f"should be agt-{{industry}}-{{scenario}}-{{name}}"
            )
        return v

    @property
    def required_capability_ids(self) -> list[str]:
        """Get all required capability IDs."""
        return [cap.id for cap in self.capabilities.required]

    @property
    def all_capability_ids(self) -> list[str]:
        """Get all capability IDs (required + optional)."""
        return self.required_capability_ids + [
            cap.id for cap in self.capabilities.optional
        ]

    @property
    def required_tool_ids(self) -> list[str]:
        """Get all required tool IDs."""
        return [t.tool_ref for t in self.tools if t.required]

    @property
    def all_tool_ids(self) -> list[str]:
        """Get all tool IDs."""
        return [t.tool_ref for t in self.tools]

    @property
    def has_escalation_rules(self) -> bool:
        """Check if agent has escalation rules defined."""
        return len(self.constraints.escalation) > 0
