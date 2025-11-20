"""Tests for taxonomy models."""

import pytest
from pydantic import ValidationError

from world_professors.models.taxonomy import Scenario, ValueFlowStage


def test_value_flow_stage_valid() -> None:
    """Test valid value flow stage creation."""
    stage = ValueFlowStage(stage="客户画像", activities=["需求调研", "风险评估"])
    assert stage.stage == "客户画像"
    assert len(stage.activities) == 2


def test_value_flow_stage_empty_activities() -> None:
    """Test that empty activities list raises error."""
    with pytest.raises(ValidationError, match="activities cannot be empty"):
        ValueFlowStage(stage="Test", activities=[])


def test_scenario_minimal() -> None:
    """Test scenario creation with minimal required fields."""
    scenario = Scenario(
        id="fin-wm-001",
        name="财富管理咨询",
        industry="金融服务",
        description="为高净值客户提供个性化资产配置建议",
    )
    assert scenario.id == "fin-wm-001"
    assert scenario.industry == "金融服务"
    assert scenario.sub_industry is None
    assert len(scenario.tags) == 0


def test_scenario_full() -> None:
    """Test scenario with all fields populated."""
    scenario = Scenario(
        id="fin-wm-001",
        name="财富管理咨询",
        industry="金融服务",
        sub_industry="资产管理",
        description="为高净值客户提供个性化资产配置建议",
        tags=["财富管理", "AI应用"],
        value_flow=[
            ValueFlowStage(stage="客户画像", activities=["需求调研", "风险评估"]),
            ValueFlowStage(stage="方案设计", activities=["市场分析", "产品筛选"]),
        ],
        key_metrics=["客户满意度", "年化收益率"],
        traditional_pain_points=["人工调研耗时长", "个性化程度低"],
        ai_opportunities=["智能问卷", "AI配置优化"],
        related_scenarios=["fin-wm-002"],
    )

    assert scenario.sub_industry == "资产管理"
    assert len(scenario.tags) == 2
    assert len(scenario.value_flow) == 2
    assert len(scenario.key_metrics) == 2
    assert len(scenario.traditional_pain_points) == 2
    assert len(scenario.ai_opportunities) == 2
    assert len(scenario.related_scenarios) == 1


def test_scenario_id_validation_valid() -> None:
    """Test valid scenario ID formats."""
    # Valid IDs
    Scenario(id="fin-wm-001", name="Test", industry="Finance", description="Test")
    Scenario(id="tech-sd-002", name="Test", industry="Tech", description="Test")
    Scenario(
        id="healthcare-diagnosis-001", name="Test", industry="Healthcare", description="Test"
    )


def test_scenario_id_validation_invalid() -> None:
    """Test invalid scenario ID format."""
    with pytest.raises(ValidationError, match="Scenario ID format error"):
        Scenario(id="invalid", name="Test", industry="Test", description="Test")

    with pytest.raises(ValidationError, match="Scenario ID format error"):
        Scenario(id="too-short", name="Test", industry="Test", description="Test")


def test_scenario_no_self_reference() -> None:
    """Test that scenario cannot reference itself."""
    with pytest.raises(ValidationError, match="related_scenarios cannot contain self ID"):
        Scenario(
            id="fin-wm-001",
            name="Test",
            industry="Finance",
            description="Test",
            related_scenarios=["fin-wm-001"],  # Self-reference
        )


def test_scenario_unique_stage_names() -> None:
    """Test that value flow stage names must be unique."""
    with pytest.raises(ValidationError, match="stage names must be unique"):
        Scenario(
            id="fin-wm-001",
            name="Test",
            industry="Finance",
            description="Test",
            value_flow=[
                ValueFlowStage(stage="客户画像", activities=["活动1"]),
                ValueFlowStage(stage="客户画像", activities=["活动2"]),  # Duplicate
            ],
        )


def test_scenario_full_path_with_sub_industry() -> None:
    """Test full_path property with sub-industry."""
    scenario = Scenario(
        id="fin-wm-001",
        name="财富管理",
        industry="金融服务",
        sub_industry="资产管理",
        description="Test",
    )
    assert scenario.full_path == "金融服务/资产管理/fin-wm-001"


def test_scenario_full_path_without_sub_industry() -> None:
    """Test full_path property without sub-industry."""
    scenario = Scenario(
        id="fin-wm-001",
        name="财富管理",
        industry="金融服务",
        description="Test",
    )
    assert scenario.full_path == "金融服务/fin-wm-001"


def test_scenario_to_yaml() -> None:
    """Test scenario YAML export."""
    scenario = Scenario(
        id="fin-wm-001",
        name="财富管理",
        industry="金融服务",
        description="测试场景",
        tags=["tag1", "tag2"],
    )
    yaml_str = scenario.to_yaml()

    assert "id: fin-wm-001" in yaml_str
    assert "name: 财富管理" in yaml_str
    assert "industry: 金融服务" in yaml_str
    assert "tags:" in yaml_str
