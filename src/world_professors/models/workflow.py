"""Workflow model for standardized business processes."""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, field_validator

from world_professors.models.base import BaseEntity


class StepType(str, Enum):
    """Workflow step automation type."""

    MANUAL = "manual"
    ASSISTED = "assisted"
    AUTOMATED = "automated"


class DataSchema(BaseModel):
    """JSON Schema-like data definition.

    Simplified schema definition for workflow step inputs/outputs.
    """

    type: str = Field(default="object")
    properties: dict[str, Any] = Field(default_factory=dict)
    required: list[str] = Field(default_factory=list)
    ref: str | None = Field(None, alias="$ref", description="Reference to schema")

    model_config = {"populate_by_name": True}


class WorkflowStep(BaseModel):
    """A step in workflow process.

    Defines input/output schemas, required tools and capabilities.
    """

    id: str = Field(..., pattern=r"^step-\d{2}$")
    name: str = Field(..., min_length=1)
    description: str | None = None
    type: StepType = StepType.MANUAL

    # Input/Output specifications
    input: DataSchema | None = Field(None, description="Input data schema")
    output: DataSchema | None = Field(None, description="Output data schema")

    # Dependencies
    depends_on: list[str] = Field(
        default_factory=list,
        description="Step IDs this step depends on",
    )

    # Required tools for this step
    tools: list[str] = Field(
        default_factory=list,
        description="Tool IDs that can be used in this step",
    )

    # Required capabilities
    capabilities: list[str] = Field(
        default_factory=list,
        description="Capability IDs required for this step",
    )

    # Timing
    estimated_duration: str | None = Field(None, description="e.g., '5min', '1h'")

    # Human checkpoint
    requires_human_confirmation: bool = Field(
        default=False,
        description="Whether this step requires human confirmation",
    )


class WorkflowMetrics(BaseModel):
    """Workflow performance metrics."""

    avg_duration: str | None = Field(None, description="Average total duration")
    automation_rate: str | None = Field(None, description="e.g., '70%'")
    success_rate: str | None = Field(None, description="e.g., '95%'")


class Workflow(BaseEntity):
    """Workflow definition model.

    Represents a standardized business process with defined steps,
    each step having clear inputs, outputs, tools, and capabilities.
    """

    # Reference
    scenario_ref: str = Field(..., description="Reference to scenario ID")

    # Steps
    steps: list[WorkflowStep] = Field(
        default_factory=list,
        min_length=1,
        description="Ordered list of workflow steps",
    )

    # Entry/Exit conditions
    entry_conditions: list[str] = Field(
        default_factory=list,
        description="Conditions that must be met to start workflow",
    )
    exit_conditions: list[str] = Field(
        default_factory=list,
        description="Conditions that indicate workflow completion",
    )

    # Human checkpoints
    human_checkpoints: list[str] = Field(
        default_factory=list,
        description="Step IDs that require human review",
    )

    # Metrics
    metrics: WorkflowMetrics | None = None

    @field_validator("id")
    @classmethod
    def validate_workflow_id(cls, v: str) -> str:
        """Validate workflow ID format: wf-{industry}-{scenario}-{name}."""
        if not v.startswith("wf-"):
            raise ValueError(f"Workflow ID must start with 'wf-': {v}")
        return v

    @property
    def step_ids(self) -> list[str]:
        """Get all step IDs in order."""
        return [step.id for step in self.steps]

    @property
    def all_tools(self) -> list[str]:
        """Get all unique tools used across steps."""
        tools: set[str] = set()
        for step in self.steps:
            tools.update(step.tools)
        return list(tools)

    @property
    def all_capabilities(self) -> list[str]:
        """Get all unique capabilities required across steps."""
        caps: set[str] = set()
        for step in self.steps:
            caps.update(step.capabilities)
        return list(caps)

    @property
    def automation_level(self) -> str:
        """Calculate overall automation level."""
        if not self.steps:
            return "unknown"

        automated = sum(1 for s in self.steps if s.type == StepType.AUTOMATED)
        assisted = sum(1 for s in self.steps if s.type == StepType.ASSISTED)
        total = len(self.steps)

        ratio = (automated + assisted * 0.5) / total
        if ratio >= 0.8:
            return "high"
        elif ratio >= 0.5:
            return "medium"
        else:
            return "low"
