"""Tests for base models."""

import pytest
from pydantic import ValidationError

from world_professors.models.base import BaseEntity, Metadata


def test_metadata_defaults() -> None:
    """Test metadata default values."""
    meta = Metadata()
    assert meta.version == "1.0"
    assert meta.schema_version == "1.0"
    assert meta.author is None
    assert meta.created_at is not None
    assert meta.updated_at is not None


def test_metadata_custom_values() -> None:
    """Test metadata with custom values."""
    meta = Metadata(author="Test Author", version="2.0")
    assert meta.author == "Test Author"
    assert meta.version == "2.0"


def test_metadata_extra_fields() -> None:
    """Test metadata allows extra fields."""
    meta = Metadata(custom_field="value")  # type: ignore[call-arg]
    assert meta.model_extra is not None
    assert meta.model_extra.get("custom_field") == "value"


def test_base_entity_valid() -> None:
    """Test valid base entity creation."""
    entity = BaseEntity(
        id="test-entity-001",
        name="Test Entity",
        description="A test entity for validation",
    )
    assert entity.id == "test-entity-001"
    assert entity.name == "Test Entity"
    assert entity.description == "A test entity for validation"
    assert entity.metadata is not None


def test_base_entity_id_validation() -> None:
    """Test ID pattern validation."""
    # Valid IDs
    BaseEntity(id="valid-id", name="Test", description="Test")
    BaseEntity(id="valid-id-123", name="Test", description="Test")
    BaseEntity(id="abc123", name="Test", description="Test")

    # Invalid IDs
    with pytest.raises(ValidationError):
        BaseEntity(id="Invalid_ID", name="Test", description="Test")  # underscore

    with pytest.raises(ValidationError):
        BaseEntity(id="Invalid ID", name="Test", description="Test")  # space

    with pytest.raises(ValidationError):
        BaseEntity(id="", name="Test", description="Test")  # empty


def test_base_entity_required_fields() -> None:
    """Test required fields validation."""
    with pytest.raises(ValidationError):
        BaseEntity(id="test")  # type: ignore[call-arg] # missing name and description

    with pytest.raises(ValidationError):
        BaseEntity(id="test", name="Test")  # type: ignore[call-arg] # missing description


def test_base_entity_name_length() -> None:
    """Test name length validation."""
    # Valid name
    BaseEntity(id="test", name="A" * 200, description="Test")

    # Too long
    with pytest.raises(ValidationError):
        BaseEntity(id="test", name="A" * 201, description="Test")


def test_base_entity_display_name() -> None:
    """Test display_name property."""
    entity = BaseEntity(id="test", name="Display Name", description="Test")
    assert entity.display_name == "Display Name"


def test_base_entity_to_dict() -> None:
    """Test to_dict method."""
    entity = BaseEntity(id="test", name="Test", description="Test description")
    data = entity.to_dict()

    assert isinstance(data, dict)
    assert data["id"] == "test"
    assert data["name"] == "Test"
    assert data["description"] == "Test description"
    assert "metadata" in data


def test_base_entity_to_yaml() -> None:
    """Test to_yaml method."""
    entity = BaseEntity(id="test", name="Test", description="Test description")
    yaml_str = entity.to_yaml()

    assert isinstance(yaml_str, str)
    assert "id: test" in yaml_str
    assert "name: Test" in yaml_str
    assert "description: Test description" in yaml_str


def test_base_entity_whitespace_stripping() -> None:
    """Test that whitespace is stripped from string fields."""
    entity = BaseEntity(
        id="test-id",
        name="  Test Name  ",
        description="  Test Description  ",
    )
    assert entity.name == "Test Name"
    assert entity.description == "Test Description"


def test_base_entity_no_extra_fields() -> None:
    """Test that base entity forbids extra fields."""
    with pytest.raises(ValidationError):
        BaseEntity(
            id="test",
            name="Test",
            description="Test",
            extra_field="not allowed",  # type: ignore[call-arg]
        )
