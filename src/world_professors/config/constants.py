"""Application constants."""

from typing import Final

# Supported industries (Tier 1)
TIER1_INDUSTRIES: Final[list[str]] = [
    "金融服务",
    "科技互联网",
    "专业服务",
]

# All supported industries
ALL_INDUSTRIES: Final[list[str]] = [
    # Tier 1
    "金融服务",
    "科技互联网",
    "专业服务",
    # Tier 2
    "医疗健康",
    "制造业",
    "教育培训",
    # Tier 3
    "零售电商",
    "文化娱乐",
    "房地产",
    "能源",
]

# Role types
ROLE_TYPES: Final[list[str]] = [
    "traditional",
    "ai-enhanced",
    "emerging",
    "ai-agent",
]

# Capability categories
CAPABILITY_CATEGORIES: Final[list[str]] = [
    "cognitive",
    "technical",
    "interpersonal",
    "domain-specific",
]

# Capability levels
CAPABILITY_LEVELS: Final[list[str]] = [
    "beginner",
    "intermediate",
    "advanced",
    "expert",
]

# AI pattern types
AI_PATTERN_TYPES: Final[list[str]] = [
    "automation",
    "augmentation",
    "generation",
    "orchestration",
]

# ID patterns (regex)
SCENARIO_ID_PATTERN: Final[str] = r"^[a-z0-9]+-[a-z0-9]+-\d{3}$"
ROLE_ID_PATTERN: Final[str] = r"^[a-z0-9]+-[a-z0-9]+-[a-z]+-[a-z0-9-]+$"
CAPABILITY_ID_PATTERN: Final[str] = r"^cap-[a-z]+-\d{3}$"

# File extensions
SUPPORTED_DATA_FORMATS: Final[list[str]] = [".yaml", ".yml"]
