"""Tests for capability models - key tests only."""
import pytest
from pydantic import ValidationError

from world_professors.models.capability import (
    Capability,
    CapabilityCategory,
    LevelDefinition,
)


def test_capability_minimal() -> None:
    """Test minimal capability."""
    cap = Capability(
        id="cap-ai-001",
        name="AI工具应用",
        category=CapabilityCategory.TECHNICAL,
        description="使用AI工具的能力",
        levels={
            "beginner": LevelDefinition(description="初级"),
            "intermediate": LevelDefinition(description="中级"),
        },
    )
    assert cap.id == "cap-ai-001"
    assert len(cap.levels) == 2

def test_capability_id_validation() -> None:
    """Test ID validation."""
    with pytest.raises(ValidationError, match="Capability ID format error"):
        Capability(
            id="invalid",
            name="Test",
            category=CapabilityCategory.TECHNICAL,
            description="Test",
            levels={"beginner": LevelDefinition(description="Test"), "intermediate": LevelDefinition(description="Test")},
        )

def test_capability_min_two_levels() -> None:
    """Test minimum two levels required."""
    with pytest.raises(ValidationError, match="At least two capability levels"):
        Capability(
            id="cap-test-001",
            name="Test",
            category=CapabilityCategory.TECHNICAL,
            description="Test",
            levels={"beginner": LevelDefinition(description="Test")},
        )
