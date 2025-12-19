"""Tests for BaseRepository.get_path()."""

from pathlib import Path

import pytest
import yaml

from world_professors.models.taxonomy import Scenario
from world_professors.repositories.base import BaseRepository, EntityNotFoundError


def test_get_path_returns_indexed_file(tmp_path: Path) -> None:
    data_dir = tmp_path / "data" / "scenarios"
    data_dir.mkdir(parents=True)

    scenario = {
        "id": "tech-saas-001",
        "name": "SaaS",
        "description": "desc",
        "industry": "Technology",
        "metadata": {"created_at": "2025-01-20T10:00:00", "updated_at": "2025-01-20T10:00:00"},
    }
    p = data_dir / "tech-saas-001.yaml"
    with open(p, "w", encoding="utf-8") as f:
        yaml.safe_dump(scenario, f)

    repo = BaseRepository(data_dir, Scenario)
    assert repo.get_path("tech-saas-001") == p


def test_get_path_not_found_raises(tmp_path: Path) -> None:
    repo = BaseRepository(tmp_path / "missing", Scenario)
    with pytest.raises(EntityNotFoundError):
        repo.get_path("nope")

