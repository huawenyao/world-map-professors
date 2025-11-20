"""Practice models for AI patterns and cases."""

from enum import Enum

from pydantic import BaseModel, Field

from world_professors.models.base import BaseEntity


class AIPatternType(str, Enum):
    """AI application pattern type."""

    AUTOMATION = "automation"
    AUGMENTATION = "augmentation"
    GENERATION = "generation"
    ORCHESTRATION = "orchestration"


class AIPattern(BaseEntity):
    """AI application pattern."""

    type: AIPatternType = Field(..., description="Pattern type")
    applicable_scenarios: list[str] = Field(
        default_factory=list, description="Applicable scenario tags"
    )
    implementation_steps: list[str] = Field(default_factory=list)
    success_factors: list[str] = Field(default_factory=list)
    common_pitfalls: list[str] = Field(default_factory=list)
    examples: list[str] = Field(default_factory=list, description="Case ID references")


class ProcessState(BaseModel):
    """Process state before or after transformation."""

    process: str = Field(..., description="Process description")
    pain_points: list[str] = Field(default_factory=list)
    metrics: dict[str, str] = Field(default_factory=dict)


class ROI(BaseModel):
    """Return on investment."""

    cost: str | None = None
    benefit: str | None = None
    payback_period: str | None = None


class TransformationCase(BaseEntity):
    """Transformation case study."""

    title: str = Field(..., min_length=1)
    industry: str = Field(..., min_length=1)
    scenario_ref: str = Field(..., description="Related scenario ID")
    summary: str = Field(..., min_length=1)

    # Before and after
    before: ProcessState
    after: ProcessState

    # Implementation
    ai_tools_used: list[str] = Field(default_factory=list)
    roi: ROI | None = None
    lessons_learned: list[str] = Field(default_factory=list)
