"""Tests for base repository."""

from pathlib import Path

import pytest
import yaml

from world_professors.models.taxonomy import Scenario
from world_professors.repositories.base import (
    BaseRepository,
    EntityNotFoundError,
    ValidationFailedError,
)


@pytest.fixture
def temp_data_dir(tmp_path: Path) -> Path:
    """Create temporary data directory with test files."""
    data_dir = tmp_path / "data" / "scenarios"
    data_dir.mkdir(parents=True)

    # Create valid scenario file
    scenario_1 = {
        "id": "tech-saas-001",
        "name": "SaaS Product Development",
        "description": "Building SaaS products",
        "industry": "Technology",
        "metadata": {
            "created_at": "2025-01-20T10:00:00",
            "updated_at": "2025-01-20T10:00:00",
        },
    }
    scenario_file_1 = data_dir / "tech-saas-001.yaml"
    with open(scenario_file_1, "w", encoding="utf-8") as f:
        yaml.dump(scenario_1, f)

    # Create another valid scenario
    scenario_2 = {
        "id": "finance-wealth-001",
        "name": "Wealth Management",
        "description": "Managing client wealth",
        "industry": "Finance",
        "metadata": {
            "created_at": "2025-01-20T10:00:00",
            "updated_at": "2025-01-20T10:00:00",
        },
    }
    scenario_file_2 = data_dir / "finance-wealth-001.yaml"
    with open(scenario_file_2, "w", encoding="utf-8") as f:
        yaml.dump(scenario_2, f)

    # Create invalid scenario (missing required field)
    invalid_scenario = {
        "id": "invalid-001",
        "name": "Invalid Scenario",
        # Missing 'description' and 'industry'
    }
    invalid_file = data_dir / "invalid-001.yaml"
    with open(invalid_file, "w", encoding="utf-8") as f:
        yaml.dump(invalid_scenario, f)

    return data_dir


def test_repository_initialization(temp_data_dir: Path) -> None:
    """Test repository initialization and index building."""
    repo = BaseRepository(temp_data_dir, Scenario)

    # Should have indexed 2 valid scenarios
    assert repo.count() == 2
    assert repo.exists("tech-saas-001")
    assert repo.exists("finance-wealth-001")
    assert not repo.exists("invalid-001")  # Invalid file skipped


def test_load_valid_entity(temp_data_dir: Path) -> None:
    """Test loading valid entity from file."""
    repo = BaseRepository(temp_data_dir, Scenario)
    scenario_file = temp_data_dir / "tech-saas-001.yaml"

    scenario = repo.load(scenario_file)

    assert scenario.id == "tech-saas-001"
    assert scenario.name == "SaaS Product Development"
    assert scenario.industry == "Technology"


def test_load_nonexistent_file(temp_data_dir: Path) -> None:
    """Test loading from nonexistent file raises error."""
    repo = BaseRepository(temp_data_dir, Scenario)
    nonexistent = temp_data_dir / "nonexistent.yaml"

    with pytest.raises(FileNotFoundError):
        repo.load(nonexistent)


def test_load_invalid_entity(temp_data_dir: Path) -> None:
    """Test loading invalid entity raises ValidationFailedError."""
    repo = BaseRepository(temp_data_dir, Scenario)
    invalid_file = temp_data_dir / "invalid-001.yaml"

    with pytest.raises(ValidationFailedError) as exc_info:
        repo.load(invalid_file)

    assert exc_info.value.file_path == invalid_file
    assert len(exc_info.value.errors) > 0


def test_load_all(temp_data_dir: Path) -> None:
    """Test loading all entities."""
    repo = BaseRepository(temp_data_dir, Scenario)

    scenarios = repo.load_all()

    assert len(scenarios) == 2
    ids = {s.id for s in scenarios}
    assert ids == {"tech-saas-001", "finance-wealth-001"}


def test_get_by_id_success(temp_data_dir: Path) -> None:
    """Test getting entity by ID."""
    repo = BaseRepository(temp_data_dir, Scenario)

    scenario = repo.get_by_id("tech-saas-001")

    assert scenario.id == "tech-saas-001"
    assert scenario.name == "SaaS Product Development"


def test_get_by_id_not_found(temp_data_dir: Path) -> None:
    """Test getting nonexistent entity raises error."""
    repo = BaseRepository(temp_data_dir, Scenario)

    with pytest.raises(EntityNotFoundError) as exc_info:
        repo.get_by_id("nonexistent-001")

    assert exc_info.value.entity_id == "nonexistent-001"
    assert exc_info.value.entity_type == "Scenario"


def test_save_existing_entity(temp_data_dir: Path) -> None:
    """Test saving existing entity (update)."""
    repo = BaseRepository(temp_data_dir, Scenario)

    # Load and modify entity
    scenario = repo.get_by_id("tech-saas-001")
    scenario.name = "Updated SaaS Product"

    # Save without specifying file_path (uses indexed path)
    saved_path = repo.save(scenario)

    # Verify changes persisted
    reloaded = repo.load(saved_path)
    assert reloaded.name == "Updated SaaS Product"


def test_save_new_entity(temp_data_dir: Path) -> None:
    """Test saving new entity."""
    repo = BaseRepository(temp_data_dir, Scenario)

    # Create new entity
    new_scenario = Scenario(
        id="retail-ecommerce-001",
        name="E-commerce Platform",
        description="Building e-commerce solutions",
        industry="Retail",
    )

    # Must specify file_path for new entity
    new_file = temp_data_dir / "retail-ecommerce-001.yaml"
    saved_path = repo.save(new_scenario, new_file)

    # Verify saved and indexed
    assert saved_path.exists()
    assert repo.exists("retail-ecommerce-001")
    assert repo.count() == 3


def test_save_new_entity_without_path_raises_error(temp_data_dir: Path) -> None:
    """Test saving new entity without file_path raises error."""
    repo = BaseRepository(temp_data_dir, Scenario)

    new_scenario = Scenario(
        id="new-scenario-001",
        name="New Scenario",
        description="Description",
        industry="Other",
    )

    with pytest.raises(ValueError, match="Cannot save new entity without file_path"):
        repo.save(new_scenario)


def test_delete_entity(temp_data_dir: Path) -> None:
    """Test deleting entity."""
    repo = BaseRepository(temp_data_dir, Scenario)

    # Verify entity exists
    assert repo.exists("tech-saas-001")
    scenario_file = temp_data_dir / "tech-saas-001.yaml"
    assert scenario_file.exists()

    # Delete entity
    repo.delete("tech-saas-001")

    # Verify deleted
    assert not repo.exists("tech-saas-001")
    assert not scenario_file.exists()
    assert repo.count() == 1


def test_delete_nonexistent_entity(temp_data_dir: Path) -> None:
    """Test deleting nonexistent entity raises error."""
    repo = BaseRepository(temp_data_dir, Scenario)

    with pytest.raises(EntityNotFoundError):
        repo.delete("nonexistent-001")


def test_exists(temp_data_dir: Path) -> None:
    """Test checking entity existence."""
    repo = BaseRepository(temp_data_dir, Scenario)

    assert repo.exists("tech-saas-001")
    assert repo.exists("finance-wealth-001")
    assert not repo.exists("nonexistent-001")


def test_count(temp_data_dir: Path) -> None:
    """Test counting entities."""
    repo = BaseRepository(temp_data_dir, Scenario)

    assert repo.count() == 2


def test_refresh_index(temp_data_dir: Path) -> None:
    """Test refreshing index after external changes."""
    repo = BaseRepository(temp_data_dir, Scenario)

    # Initial count
    assert repo.count() == 2

    # Add new file externally
    new_scenario = {
        "id": "healthcare-telemedicine-001",
        "name": "Telemedicine",
        "description": "Remote healthcare services",
        "industry": "Healthcare",
        "metadata": {
            "created_at": "2025-01-20T10:00:00",
            "updated_at": "2025-01-20T10:00:00",
        },
    }
    new_file = temp_data_dir / "healthcare-telemedicine-001.yaml"
    with open(new_file, "w", encoding="utf-8") as f:
        yaml.dump(new_scenario, f)

    # Before refresh, not indexed
    assert not repo.exists("healthcare-telemedicine-001")

    # After refresh, should be indexed
    repo.refresh()
    assert repo.exists("healthcare-telemedicine-001")
    assert repo.count() == 3


def test_empty_data_dir(tmp_path: Path) -> None:
    """Test repository with non-existent data directory."""
    nonexistent_dir = tmp_path / "nonexistent"

    repo = BaseRepository(nonexistent_dir, Scenario)

    assert repo.count() == 0
    assert repo.load_all() == []
