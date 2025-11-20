"""Taxonomy models for industries and scenarios."""

from typing import Any

from pydantic import BaseModel, Field, field_validator

from world_professors.models.base import BaseEntity


class ValueFlowStage(BaseModel):
    """A stage in the value flow."""

    stage: str = Field(..., min_length=1, description="Stage name")
    activities: list[str] = Field(default_factory=list, description="Activities in this stage")

    @field_validator("activities")
    @classmethod
    def validate_activities(cls, v: list[str]) -> list[str]:
        """Validate that activities list is not empty."""
        if not v:
            raise ValueError("activities cannot be empty")
        return v


class Scenario(BaseEntity):
    """Business scenario model."""

    # Basic information
    industry: str = Field(..., description="Industry this scenario belongs to")
    sub_industry: str | None = Field(None, description="Sub-industry classification")
    tags: list[str] = Field(default_factory=list, description="Searchable tags")

    # Value flow
    value_flow: list[ValueFlowStage] = Field(
        default_factory=list, description="Value creation flow"
    )

    # Key information
    key_metrics: list[str] = Field(default_factory=list, description="Key performance metrics")
    traditional_pain_points: list[str] = Field(
        default_factory=list, description="Pain points in traditional approach"
    )
    ai_opportunities: list[str] = Field(
        default_factory=list, description="Opportunities for AI application"
    )

    # Relationships
    related_scenarios: list[str] = Field(
        default_factory=list, description="Related scenario IDs"
    )

    @field_validator("id")
    @classmethod
    def validate_scenario_id(cls, v: str) -> str:
        """Validate scenario ID format: {industry}-{scenario}-{num}."""
        parts = v.split("-")
        if len(parts) < 3:
            raise ValueError(
                f"Scenario ID format error: {v}, "
                f"should be {{industry}}-{{scenario}}-{{num}}"
            )
        return v

    @field_validator("related_scenarios")
    @classmethod
    def no_self_reference(cls, v: list[str], info: Any) -> list[str]:
        """Prevent self-reference in related scenarios."""
        if info.data and info.data.get("id") in v:
            raise ValueError("related_scenarios cannot contain self ID")
        return v

    @field_validator("value_flow")
    @classmethod
    def unique_stage_names(cls, v: list[ValueFlowStage]) -> list[ValueFlowStage]:
        """Ensure stage names are unique."""
        stages = [stage.stage for stage in v]
        if len(stages) != len(set(stages)):
            raise ValueError("Value flow stage names must be unique")
        return v

    @property
    def full_path(self) -> str:
        """Get full scenario path."""
        if self.sub_industry:
            return f"{self.industry}/{self.sub_industry}/{self.id}"
        return f"{self.industry}/{self.id}"
