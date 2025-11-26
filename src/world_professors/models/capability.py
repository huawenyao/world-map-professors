"""Capability models for skills and competencies."""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, field_validator

from world_professors.models.base import BaseEntity


class CapabilityCategory(str, Enum):
    """Capability category classification."""

    COGNITIVE = "cognitive"
    TECHNICAL = "technical"
    INTERPERSONAL = "interpersonal"
    DOMAIN_SPECIFIC = "domain-specific"


class Transferability(str, Enum):
    """Transferability level across contexts."""

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class AIImpact(str, Enum):
    """AI's impact on this capability."""

    ENHANCED = "enhanced"  # Enhanced by AI
    AUGMENTED = "augmented"  # Augmented/extended
    AUTOMATED = "automated"  # Can be automated
    OBSOLETE = "obsolete"  # Becoming obsolete


class LevelDefinition(BaseModel):
    """Definition of a proficiency level."""

    description: str = Field(..., min_length=1)
    skills: list[str] = Field(default_factory=list)
    tasks: list[str] = Field(default_factory=list)


class LearningResources(BaseModel):
    """Learning resources for capability development."""

    courses: list[str] = Field(default_factory=list)
    books: list[str] = Field(default_factory=list)
    practice: list[str] = Field(default_factory=list)


class Milestone(BaseModel):
    """Learning milestone."""

    month: int = Field(..., ge=1, le=60, description="Timeline in months")
    goal: str = Field(..., min_length=1)


class LearningPath(BaseModel):
    """Learning path for capability development."""

    prerequisites: list[str] = Field(
        default_factory=list, description="Prerequisite capability IDs"
    )
    estimated_time: str | None = Field(None, description="e.g., '3 months', '6-12 months'")
    resources: LearningResources | None = None
    milestones: list[Milestone] = Field(default_factory=list)


class TransferabilityProfile(BaseModel):
    """Transferability profile across contexts."""

    across_industries: Transferability = Transferability.MEDIUM
    across_scenarios: Transferability = Transferability.MEDIUM


class Capability(BaseEntity):
    """Capability/skill model."""

    # Naming
    name_en: str | None = Field(None, description="English name")

    # Classification
    category: CapabilityCategory = Field(..., description="Capability category")
    sub_category: str | None = Field(None, description="Sub-category classification")
    aliases: list[str] = Field(default_factory=list, description="Alternative names")

    # Level definitions
    levels: dict[str, LevelDefinition] = Field(
        default_factory=dict, description="Proficiency level definitions"
    )

    # Learning path
    learning_path: LearningPath | None = None

    # Relationships
    related_capabilities: list[str] = Field(
        default_factory=list, description="Related capability IDs"
    )
    applicable_roles: list[str] = Field(
        default_factory=list, description="Applicable roles (descriptive)"
    )

    # Characteristics
    transferability: TransferabilityProfile | None = None
    ai_impact: AIImpact | None = None

    @field_validator("id")
    @classmethod
    def validate_capability_id(cls, v: str) -> str:
        """Validate capability ID format: cap-{category}-{num}."""
        import re

        if not re.match(r"^cap-[a-z]+-\d{3}$", v):
            raise ValueError(
                f"Capability ID format error: {v}, " f"should be cap-{{category}}-{{num}}"
            )
        return v

    @field_validator("levels")
    @classmethod
    def validate_levels(cls, v: dict[str, LevelDefinition]) -> dict[str, LevelDefinition]:
        """Validate that at least two levels are defined."""
        if len(v) < 2:
            raise ValueError("At least two capability levels must be defined")

        valid_levels = {"beginner", "intermediate", "advanced", "expert"}
        invalid = set(v.keys()) - valid_levels
        if invalid:
            raise ValueError(f"Invalid level names: {invalid}")

        return v

    @field_validator("related_capabilities")
    @classmethod
    def no_self_reference(cls, v: list[str], info: Any) -> list[str]:
        """Prevent self-reference in related capabilities."""
        if info.data and info.data.get("id") in v:
            raise ValueError("related_capabilities cannot contain self ID")
        return v

    @property
    def level_names(self) -> list[str]:
        """Get all defined level names."""
        return list(self.levels.keys())

    @property
    def has_learning_path(self) -> bool:
        """Check if learning path is defined."""
        return self.learning_path is not None
