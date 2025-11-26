"""Data models for World Professors - Industry Agent Standard Library.

Core Models:
- Industry: Top-level industry classification
- Scenario: Business scenarios within industries
- Workflow: Standardized business processes with steps
- Agent: AI agent definitions with capabilities and tools
- Capability: Skills and competencies
- Tool: AI tools and APIs with interface specifications
"""

from world_professors.models.base import BaseEntity, Metadata

# New: Industry model
from world_professors.models.industry import (
    AIMaturity,
    DataSensitivity,
    Industry,
    IndustryCharacteristics,
    RegulatoryLevel,
    SubIndustry,
)

# Taxonomy (Scenario)
from world_professors.models.taxonomy import Scenario, ValueFlowStage

# New: Workflow model
from world_professors.models.workflow import (
    DataSchema,
    Workflow,
    WorkflowMetrics,
    WorkflowStep,
    StepType,
)

# New: Agent model (upgraded from Role.AI_AGENT)
from world_professors.models.agent import (
    Agent,
    AgentCapabilities,
    AgentConstraints,
    AgentInterface,
    AgentMetrics,
    AgentType,
    EscalationRule,
    InterfaceSchema,
    QualityMetric,
    EfficiencyMetric,
    ToolReference,
)

# New: Tool model (independent from Role.AITool)
from world_professors.models.tool import (
    AuthenticationType,
    Endpoint,
    InterfaceType,
    Parameter,
    PricingModel,
    Provider,
    RateLimit,
    Tool,
    ToolAuthentication,
    ToolCategory,
    ToolInterface,
    ToolPricing,
    ToolRequirements,
)

# Role (for human roles, legacy support)
from world_professors.models.role import (
    AITool,
    AutomationLevel,
    CapabilityLevel,
    Priority,
    RequiredCapability,
    Responsibilities,
    Role,
    RoleType,
    SalaryRange,
    TransformationImpact,
    WorkflowStep as RoleWorkflowStep,  # Renamed to avoid conflict
)

# Capability
from world_professors.models.capability import (
    AIImpact,
    Capability,
    CapabilityCategory,
    LearningPath,
    LevelDefinition,
    Milestone,
    Transferability,
)

# Practice (patterns and cases)
from world_professors.models.practice import (
    ROI,
    AIPattern,
    AIPatternType,
    ProcessState,
    TransformationCase,
)

__all__ = [
    # === Core Models ===
    # Base
    "BaseEntity",
    "Metadata",
    # Industry (NEW)
    "Industry",
    "SubIndustry",
    "IndustryCharacteristics",
    "RegulatoryLevel",
    "DataSensitivity",
    "AIMaturity",
    # Scenario
    "Scenario",
    "ValueFlowStage",
    # Workflow (NEW)
    "Workflow",
    "WorkflowStep",
    "StepType",
    "DataSchema",
    "WorkflowMetrics",
    # Agent (NEW - upgraded)
    "Agent",
    "AgentType",
    "AgentCapabilities",
    "AgentInterface",
    "AgentConstraints",
    "AgentMetrics",
    "ToolReference",
    "EscalationRule",
    "InterfaceSchema",
    "QualityMetric",
    "EfficiencyMetric",
    # Tool (NEW - independent)
    "Tool",
    "ToolCategory",
    "ToolInterface",
    "InterfaceType",
    "Endpoint",
    "Parameter",
    "ToolRequirements",
    "ToolAuthentication",
    "AuthenticationType",
    "RateLimit",
    "ToolPricing",
    "PricingModel",
    "Provider",
    # Capability
    "Capability",
    "CapabilityCategory",
    "CapabilityLevel",
    "LevelDefinition",
    "LearningPath",
    "Milestone",
    "Transferability",
    "AIImpact",
    # === Legacy/Supporting Models ===
    # Role (human roles)
    "Role",
    "RoleType",
    "RequiredCapability",
    "Priority",
    "Responsibilities",
    "AITool",
    "RoleWorkflowStep",
    "AutomationLevel",
    "TransformationImpact",
    "SalaryRange",
    # Practice
    "AIPattern",
    "AIPatternType",
    "TransformationCase",
    "ProcessState",
    "ROI",
]
