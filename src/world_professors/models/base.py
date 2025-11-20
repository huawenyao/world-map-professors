"""Base models for all entities."""

from datetime import datetime
from typing import Any

import yaml
from pydantic import BaseModel, ConfigDict, Field


class Metadata(BaseModel):
    """Metadata for all entities."""

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    author: str | None = None
    version: str = "1.0"
    schema_version: str = "1.0"

    model_config = ConfigDict(
        extra="allow",  # 允许额外字段(扩展性)
        validate_assignment=True,
    )


class BaseEntity(BaseModel):
    """Base class for all entities."""

    id: str = Field(..., pattern=r"^[a-z0-9-]+$", min_length=1)
    name: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=1)
    metadata: Metadata = Field(default_factory=Metadata)

    model_config = ConfigDict(
        extra="forbid",  # 默认不允许额外字段(严格模式)
        validate_assignment=True,
        str_strip_whitespace=True,
    )

    @property
    def display_name(self) -> str:
        """Return display name."""
        return self.name

    def to_yaml(self) -> str:
        """Export to YAML string."""
        data = self.model_dump(exclude_none=True, by_alias=True)
        return yaml.dump(data, allow_unicode=True, sort_keys=False)

    def to_dict(self) -> dict[str, Any]:
        """Export to dictionary."""
        return self.model_dump(exclude_none=True)
