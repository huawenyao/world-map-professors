"""Configuration management."""

from world_professors.config.constants import (
    AI_PATTERN_TYPES,
    ALL_INDUSTRIES,
    CAPABILITY_CATEGORIES,
    CAPABILITY_ID_PATTERN,
    CAPABILITY_LEVELS,
    ROLE_ID_PATTERN,
    ROLE_TYPES,
    SCENARIO_ID_PATTERN,
    SUPPORTED_DATA_FORMATS,
    TIER1_INDUSTRIES,
)
from world_professors.config.settings import Settings, settings

__all__ = [
    "Settings",
    "settings",
    "ALL_INDUSTRIES",
    "TIER1_INDUSTRIES",
    "ROLE_TYPES",
    "CAPABILITY_CATEGORIES",
    "CAPABILITY_LEVELS",
    "AI_PATTERN_TYPES",
    "SCENARIO_ID_PATTERN",
    "ROLE_ID_PATTERN",
    "CAPABILITY_ID_PATTERN",
    "SUPPORTED_DATA_FORMATS",
]
