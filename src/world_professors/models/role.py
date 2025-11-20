"""Role models for digital roles in AI era."""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, field_validator, model_validator

from world_professors.models.base import BaseEntity


class RoleType(str, Enum):
    """Role type classification."""

    TRADITIONAL = "traditional"
    AI_ENHANCED = "ai-enhanced"
    EMERGING = "emerging"
    AI_AGENT = "ai-agent"


class CapabilityLevel(str, Enum):
    """Capability proficiency level."""

    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"


class Priority(str, Enum):
    """Priority level for capabilities."""

    MUST_HAVE = "must-have"
    SHOULD_HAVE = "should-have"
    NICE_TO_HAVE = "nice-to-have"


class AutomationLevel(str, Enum):
    """Automation level for workflow steps."""

    MANUAL = "manual"
    ASSISTED = "assisted"
    AUTOMATED = "automated"


class RequiredCapability(BaseModel):
    """Capability requirement for a role."""

    capability_id: str = Field(..., pattern=r"^cap-[a-z]+-\d{3}$")
    level: CapabilityLevel
    priority: Priority = Priority.SHOULD_HAVE


class Responsibilities(BaseModel):
    """Responsibility distribution between human and AI."""

    core: list[str] = Field(default_factory=list, description="AI cannot replace")
    delegated_to_ai: list[str] = Field(default_factory=list, description="Delegated to AI")
    collaborative: list[str] = Field(
        default_factory=list, description="Human-AI collaboration"
    )


class AITool(BaseModel):
    """AI tool used in the role."""

    name: str = Field(..., min_length=1)
    purpose: str = Field(..., min_length=1)
    vendor: list[str] = Field(default_factory=list)
    cost: str | None = Field(None, pattern=r"^(free|freemium|paid)$")


class WorkflowStep(BaseModel):
    """A step in typical workflow."""

    step: str = Field(..., min_length=1)
    human_time: str | None = None
    ai_time: str | None = None
    automation_level: AutomationLevel | None = None


class TransformationImpact(BaseModel):
    """Impact of AI transformation on the role."""

    efficiency_gain: str | None = Field(None, description="e.g., '3x', '50%'")
    quality_improvement: str | None = Field(None, description="Quality metrics improvement")
    new_capabilities: list[str] = Field(default_factory=list)
    obsolete_skills: list[str] = Field(default_factory=list)


class SalaryRange(BaseModel):
    """Salary range for the role."""

    min: int = Field(..., gt=0)
    max: int = Field(..., gt=0)
    currency: str = Field(default="CNY")
    region: str = Field(default="China")

    @field_validator("max")
    @classmethod
    def max_greater_than_min(cls, v: int, info: Any) -> int:
        """Validate max is greater than min."""
        if info.data and "min" in info.data and v < info.data["min"]:
            raise ValueError("max must be greater than min")
        return v


class Role(BaseEntity):
    """Digital role model in AI era."""

    # Basic classification
    type: RoleType = Field(..., description="Role type classification")
    scenario_ref: str = Field(..., description="Reference to scenario ID")

    # AI-enhanced specific field
    traditional_role: str | None = Field(
        None, description="Traditional role name (required for ai-enhanced)"
    )

    # Responsibilities and capabilities
    responsibilities: Responsibilities | None = None
    required_capabilities: list[RequiredCapability] = Field(default_factory=list)

    # AI tools and workflow
    ai_tools: list[AITool] = Field(default_factory=list)
    typical_workflow: list[WorkflowStep] = Field(default_factory=list)

    # Transformation impact
    transformation_impact: TransformationImpact | None = None

    # Compensation
    salary_range: SalaryRange | None = None

    @field_validator("id")
    @classmethod
    def validate_role_id(cls, v: str) -> str:
        """Validate role ID format: {industry}-{scenario}-{type}-{name}."""
        parts = v.split("-")
        if len(parts) < 4:
            raise ValueError(
                f"Role ID format error: {v}, "
                f"should be {{industry}}-{{scenario}}-{{type}}-{{name}}"
            )
        return v

    @model_validator(mode="after")
    def validate_traditional_role_for_ai_enhanced(self) -> "Role":
        """Validate that ai-enhanced roles must specify traditional_role."""
        if self.type == RoleType.AI_ENHANCED and not self.traditional_role:
            raise ValueError("traditional_role is required for ai-enhanced type")
        return self

    @property
    def capability_ids(self) -> list[str]:
        """Extract all capability IDs."""
        return [cap.capability_id for cap in self.required_capabilities]

    @property
    def has_ai_tools(self) -> bool:
        """Check if role uses AI tools."""
        return len(self.ai_tools) > 0
