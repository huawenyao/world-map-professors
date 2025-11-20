"""Tests for role models."""

import pytest
from pydantic import ValidationError

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
    WorkflowStep,
)


def test_required_capability_valid() -> None:
    """Test valid required capability."""
    cap = RequiredCapability(
        capability_id="cap-ai-001", level=CapabilityLevel.INTERMEDIATE
    )
    assert cap.capability_id == "cap-ai-001"
    assert cap.level == CapabilityLevel.INTERMEDIATE
    assert cap.priority == Priority.SHOULD_HAVE  # default


def test_required_capability_invalid_id() -> None:
    """Test invalid capability ID format."""
    with pytest.raises(ValidationError):
        RequiredCapability(capability_id="invalid", level=CapabilityLevel.BEGINNER)


def test_responsibilities_model() -> None:
    """Test responsibilities model."""
    resp = Responsibilities(
        core=["决策", "沟通"],
        delegated_to_ai=["数据收集"],
        collaborative=["分析"],
    )
    assert len(resp.core) == 2
    assert len(resp.delegated_to_ai) == 1
    assert len(resp.collaborative) == 1


def test_ai_tool_valid() -> None:
    """Test AI tool model."""
    tool = AITool(
        name="ChatGPT",
        purpose="内容生成",
        vendor=["OpenAI"],
        cost="paid",
    )
    assert tool.name == "ChatGPT"
    assert tool.cost == "paid"


def test_ai_tool_invalid_cost() -> None:
    """Test invalid cost value."""
    with pytest.raises(ValidationError):
        AITool(name="Test", purpose="Test", cost="invalid")


def test_workflow_step() -> None:
    """Test workflow step model."""
    step = WorkflowStep(
        step="数据分析",
        human_time="30min",
        ai_time="5sec",
        automation_level=AutomationLevel.ASSISTED,
    )
    assert step.step == "数据分析"
    assert step.automation_level == AutomationLevel.ASSISTED


def test_salary_range_valid() -> None:
    """Test valid salary range."""
    salary = SalaryRange(min=200000, max=500000)
    assert salary.min == 200000
    assert salary.max == 500000
    assert salary.currency == "CNY"


def test_salary_range_max_less_than_min() -> None:
    """Test that max must be greater than min."""
    with pytest.raises(ValidationError, match="max must be greater than min"):
        SalaryRange(min=500000, max=200000)


def test_transformation_impact() -> None:
    """Test transformation impact model."""
    impact = TransformationImpact(
        efficiency_gain="3x",
        quality_improvement="+25%",
        new_capabilities=["AI协作"],
        obsolete_skills=["手工计算"],
    )
    assert impact.efficiency_gain == "3x"
    assert len(impact.new_capabilities) == 1


def test_role_minimal_traditional() -> None:
    """Test minimal traditional role creation."""
    role = Role(
        id="fin-wm-trad-advisor",
        name="传统财富顾问",
        type=RoleType.TRADITIONAL,
        scenario_ref="fin-wm-001",
        description="传统的财富管理顾问",
    )
    assert role.type == RoleType.TRADITIONAL
    assert role.traditional_role is None  # not required for traditional


def test_role_ai_enhanced_requires_traditional_role() -> None:
    """Test that ai-enhanced role requires traditional_role."""
    with pytest.raises(ValidationError, match="traditional_role is required"):
        Role(
            id="fin-wm-ai-advisor",
            name="AI财富顾问",
            type=RoleType.AI_ENHANCED,
            scenario_ref="fin-wm-001",
            description="AI增强的财富顾问",
            # Missing traditional_role
        )


def test_role_ai_enhanced_valid() -> None:
    """Test valid ai-enhanced role."""
    role = Role(
        id="fin-wm-ai-advisor",
        name="AI财富顾问",
        type=RoleType.AI_ENHANCED,
        scenario_ref="fin-wm-001",
        description="AI增强的财富顾问",
        traditional_role="传统财富顾问",
    )
    assert role.traditional_role == "传统财富顾问"


def test_role_full_featured() -> None:
    """Test role with all features."""
    role = Role(
        id="fin-wm-ai-advisor",
        name="AI财富顾问",
        type=RoleType.AI_ENHANCED,
        scenario_ref="fin-wm-001",
        description="结合AI工具的财富管理顾问",
        traditional_role="传统财富顾问",
        responsibilities=Responsibilities(
            core=["客户沟通", "决策"],
            delegated_to_ai=["数据收集"],
            collaborative=["方案设计"],
        ),
        required_capabilities=[
            RequiredCapability(
                capability_id="cap-fin-001",
                level=CapabilityLevel.EXPERT,
                priority=Priority.MUST_HAVE,
            ),
            RequiredCapability(
                capability_id="cap-ai-003",
                level=CapabilityLevel.INTERMEDIATE,
            ),
        ],
        ai_tools=[
            AITool(name="AI配置引擎", purpose="资产配置优化", cost="paid"),
        ],
        typical_workflow=[
            WorkflowStep(
                step="客户画像",
                human_time="10min",
                ai_time="实时",
                automation_level=AutomationLevel.AUTOMATED,
            ),
        ],
        transformation_impact=TransformationImpact(
            efficiency_gain="3x",
            new_capabilities=["服务更多客户"],
        ),
        salary_range=SalaryRange(min=300000, max=800000),
    )

    assert len(role.required_capabilities) == 2
    assert len(role.ai_tools) == 1
    assert len(role.typical_workflow) == 1
    assert role.salary_range is not None


def test_role_id_validation_valid() -> None:
    """Test valid role ID formats."""
    Role(
        id="fin-wm-trad-advisor",
        name="Test",
        type=RoleType.TRADITIONAL,
        scenario_ref="fin-wm-001",
        description="Test",
    )
    Role(
        id="tech-sd-ai-engineer",
        name="Test",
        type=RoleType.AI_ENHANCED,
        scenario_ref="tech-sd-001",
        description="Test",
        traditional_role="Engineer",
    )


def test_role_id_validation_invalid() -> None:
    """Test invalid role ID format."""
    with pytest.raises(ValidationError, match="Role ID format error"):
        Role(
            id="invalid",
            name="Test",
            type=RoleType.TRADITIONAL,
            scenario_ref="test",
            description="Test",
        )


def test_role_capability_ids_property() -> None:
    """Test capability_ids property."""
    role = Role(
        id="fin-wm-trad-advisor",
        name="Test",
        type=RoleType.TRADITIONAL,
        scenario_ref="fin-wm-001",
        description="Test",
        required_capabilities=[
            RequiredCapability(capability_id="cap-fin-001", level=CapabilityLevel.EXPERT),
            RequiredCapability(capability_id="cap-ai-003", level=CapabilityLevel.BEGINNER),
        ],
    )
    assert role.capability_ids == ["cap-fin-001", "cap-ai-003"]


def test_role_has_ai_tools_property() -> None:
    """Test has_ai_tools property."""
    role_without = Role(
        id="fin-wm-trad-advisor",
        name="Test",
        type=RoleType.TRADITIONAL,
        scenario_ref="fin-wm-001",
        description="Test",
    )
    assert role_without.has_ai_tools is False

    role_with = Role(
        id="fin-wm-ai-advisor",
        name="Test",
        type=RoleType.AI_ENHANCED,
        scenario_ref="fin-wm-001",
        description="Test",
        traditional_role="Advisor",
        ai_tools=[AITool(name="Tool", purpose="Purpose")],
    )
    assert role_with.has_ai_tools is True
