"""Industry model for industry classification."""

from enum import Enum

from pydantic import BaseModel, Field

from world_professors.models.base import BaseEntity


class RegulatoryLevel(str, Enum):
    """Regulatory level classification."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class DataSensitivity(str, Enum):
    """Data sensitivity level."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class AIMaturity(str, Enum):
    """AI adoption maturity level."""

    NASCENT = "nascent"
    EMERGING = "emerging"
    MEDIUM = "medium"
    ADVANCED = "advanced"
    MATURE = "mature"


class SubIndustry(BaseModel):
    """Sub-industry definition."""

    id: str = Field(..., pattern=r"^ind-[a-z]+-[a-z-]+$")
    name: str = Field(..., min_length=1)
    name_en: str | None = None
    description: str | None = None


class IndustryCharacteristics(BaseModel):
    """Industry characteristics."""

    regulatory_level: RegulatoryLevel = RegulatoryLevel.MEDIUM
    data_sensitivity: DataSensitivity = DataSensitivity.MEDIUM
    ai_maturity: AIMaturity = AIMaturity.MEDIUM
    automation_potential: str | None = Field(
        None, description="e.g., 'high', 'medium', 'low'"
    )


class Industry(BaseEntity):
    """Industry definition model.

    Represents a top-level industry classification with sub-industries,
    characteristics, and common capability requirements.
    """

    # Naming
    name_en: str | None = Field(None, description="English name")

    # Sub-industries
    sub_industries: list[SubIndustry] = Field(default_factory=list)

    # Characteristics
    characteristics: IndustryCharacteristics | None = None

    # Common capabilities required across this industry
    common_capabilities: list[str] = Field(
        default_factory=list,
        description="Capability IDs common to this industry",
    )

    # Related industries
    related_industries: list[str] = Field(
        default_factory=list,
        description="Related industry IDs",
    )

    @property
    def sub_industry_ids(self) -> list[str]:
        """Get all sub-industry IDs."""
        return [sub.id for sub in self.sub_industries]
