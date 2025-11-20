"""Integration tests for role repository."""

from pathlib import Path

import pytest
import yaml

from world_professors.models.role import RoleType
from world_professors.repositories.role_repo import RoleRepository


@pytest.fixture
def role_data_dir(tmp_path: Path) -> Path:
    """Create test data directory with role files."""
    data_dir = tmp_path / "data"
    roles_dir = data_dir / "roles" / "by-industry"
    roles_dir.mkdir(parents=True)

    roles = [
        # Traditional role
        {
            "id": "tech-saas-traditional-pm",
            "name": "Product Manager",
            "description": "Traditional product management role",
            "type": "traditional",
            "scenario_ref": "tech-saas-product-001",
            "required_capabilities": [],
            "ai_tools": [],
            "typical_workflow": [],
            "metadata": {
                "created_at": "2025-01-20T10:00:00",
                "updated_at": "2025-01-20T10:00:00",
            },
        },
        # AI-enhanced role
        {
            "id": "tech-saas-ai-enhanced-pm",
            "name": "AI-Enhanced Product Manager",
            "description": "Product manager using AI tools",
            "type": "ai-enhanced",
            "traditional_role": "Product Manager",
            "scenario_ref": "tech-saas-product-001",
            "required_capabilities": [
                {"capability_id": "cap-cognitive-001", "level": "advanced"},
            ],
            "ai_tools": [
                {"name": "Claude", "purpose": "Requirements analysis", "vendor": ["Anthropic"]},
                {"name": "GitHub Copilot", "purpose": "Code review", "vendor": ["GitHub"]},
            ],
            "typical_workflow": [],
            "metadata": {
                "created_at": "2025-01-20T10:00:00",
                "updated_at": "2025-01-20T10:00:00",
            },
        },
        # Emerging role
        {
            "id": "tech-ai-emerging-prompt-eng",
            "name": "Prompt Engineer",
            "description": "AI prompt engineering specialist",
            "type": "emerging",
            "scenario_ref": "tech-ai-development-001",
            "required_capabilities": [
                {"capability_id": "cap-technical-002", "level": "expert"},
            ],
            "ai_tools": [
                {"name": "GPT-4", "purpose": "Testing prompts", "vendor": ["OpenAI"]},
            ],
            "typical_workflow": [],
            "metadata": {
                "created_at": "2025-01-20T10:00:00",
                "updated_at": "2025-01-20T10:00:00",
            },
        },
        # AI agent role
        {
            "id": "service-support-ai-agent-cs",
            "name": "AI Customer Service Agent",
            "description": "Automated customer service",
            "type": "ai-agent",
            "scenario_ref": "service-customer-support-001",
            "required_capabilities": [],
            "ai_tools": [
                {"name": "Claude", "purpose": "Customer interaction", "vendor": ["Anthropic"]},
            ],
            "typical_workflow": [],
            "metadata": {
                "created_at": "2025-01-20T10:00:00",
                "updated_at": "2025-01-20T10:00:00",
            },
        },
        # Finance role
        {
            "id": "finance-wealth-ai-enhanced-advisor",
            "name": "AI Wealth Advisor",
            "description": "AI-powered wealth advisory",
            "type": "ai-enhanced",
            "traditional_role": "Wealth Advisor",
            "scenario_ref": "finance-wealth-mgmt-001",
            "required_capabilities": [
                {"capability_id": "cap-cognitive-001", "level": "intermediate"},
            ],
            "ai_tools": [],
            "typical_workflow": [],
            "metadata": {
                "created_at": "2025-01-20T10:00:00",
                "updated_at": "2025-01-20T10:00:00",
            },
        },
    ]

    for role in roles:
        file_path = roles_dir / f"{role['id']}.yaml"
        with open(file_path, "w", encoding="utf-8") as f:
            yaml.dump(role, f)

    return data_dir


def test_initialization(role_data_dir: Path) -> None:
    """Test repository initialization."""
    repo = RoleRepository(role_data_dir)

    assert repo.count() == 5
    assert repo.exists("tech-saas-traditional-pm")
    assert repo.exists("tech-saas-ai-enhanced-pm")


def test_get_by_scenario(role_data_dir: Path) -> None:
    """Test filtering roles by scenario."""
    repo = RoleRepository(role_data_dir)

    saas_roles = repo.get_by_scenario("tech-saas-product-001")
    assert len(saas_roles) == 2
    ids = {r.id for r in saas_roles}
    assert ids == {"tech-saas-traditional-pm", "tech-saas-ai-enhanced-pm"}


def test_get_by_type(role_data_dir: Path) -> None:
    """Test filtering roles by type."""
    repo = RoleRepository(role_data_dir)

    ai_enhanced = repo.get_by_type(RoleType.AI_ENHANCED)
    assert len(ai_enhanced) == 2

    traditional = repo.get_by_type(RoleType.TRADITIONAL)
    assert len(traditional) == 1

    emerging = repo.get_by_type(RoleType.EMERGING)
    assert len(emerging) == 1

    ai_agent = repo.get_by_type(RoleType.AI_AGENT)
    assert len(ai_agent) == 1


def test_get_by_industry(role_data_dir: Path) -> None:
    """Test filtering roles by industry."""
    repo = RoleRepository(role_data_dir)

    tech_roles = repo.get_by_industry("tech")
    assert len(tech_roles) == 3  # 2 SaaS + 1 AI dev

    finance_roles = repo.get_by_industry("finance")
    assert len(finance_roles) == 1


def test_get_ai_enhanced_roles(role_data_dir: Path) -> None:
    """Test getting AI-enhanced roles."""
    repo = RoleRepository(role_data_dir)

    ai_enhanced = repo.get_ai_enhanced_roles()
    assert len(ai_enhanced) == 2


def test_get_by_capability(role_data_dir: Path) -> None:
    """Test filtering roles by required capability."""
    repo = RoleRepository(role_data_dir)

    roles_with_cap = repo.get_by_capability("cap-cognitive-001")
    assert len(roles_with_cap) == 2

    roles_with_tech_cap = repo.get_by_capability("cap-technical-002")
    assert len(roles_with_tech_cap) == 1


def test_get_by_ai_tool(role_data_dir: Path) -> None:
    """Test filtering roles by AI tool."""
    repo = RoleRepository(role_data_dir)

    claude_roles = repo.get_by_ai_tool("Claude")
    assert len(claude_roles) == 2

    copilot_roles = repo.get_by_ai_tool("Copilot")
    assert len(copilot_roles) == 1

    gpt_roles = repo.get_by_ai_tool("GPT")
    assert len(gpt_roles) == 1


def test_list_scenarios(role_data_dir: Path) -> None:
    """Test listing all scenario references."""
    repo = RoleRepository(role_data_dir)

    scenarios = repo.list_scenarios()
    assert len(scenarios) == 4
    assert "tech-saas-product-001" in scenarios
    assert "finance-wealth-mgmt-001" in scenarios


def test_list_traditional_roles(role_data_dir: Path) -> None:
    """Test listing all traditional role names."""
    repo = RoleRepository(role_data_dir)

    traditional = repo.list_traditional_roles()
    assert len(traditional) == 2
    assert "Product Manager" in traditional
    assert "Wealth Advisor" in traditional


def test_search(role_data_dir: Path) -> None:
    """Test searching roles."""
    repo = RoleRepository(role_data_dir)

    # Search by name
    pm_results = repo.search("Product Manager")
    assert len(pm_results) == 2

    # Search by description (case-insensitive)
    ai_results = repo.search("ai")
    assert len(ai_results) >= 3

    # No match
    no_results = repo.search("nonexistent")
    assert len(no_results) == 0


def test_get_role_count_by_type(role_data_dir: Path) -> None:
    """Test counting roles by type."""
    repo = RoleRepository(role_data_dir)

    counts = repo.get_role_count_by_type()

    assert counts[RoleType.TRADITIONAL] == 1
    assert counts[RoleType.AI_ENHANCED] == 2
    assert counts[RoleType.EMERGING] == 1
    assert counts[RoleType.AI_AGENT] == 1
