"""Pytest configuration and shared fixtures."""

from pathlib import Path

import pytest


@pytest.fixture
def test_data_dir() -> Path:
    """Test data directory."""
    return Path(__file__).parent / "fixtures"


@pytest.fixture
def temp_data_dir(tmp_path: Path) -> Path:
    """Temporary data directory for tests."""
    return tmp_path / "data"
