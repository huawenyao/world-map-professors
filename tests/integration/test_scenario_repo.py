"""Integration tests for scenario repository."""

from pathlib import Path

import pytest
import yaml

from world_professors.repositories.scenario_repo import ScenarioRepository


@pytest.fixture
def scenario_data_dir(tmp_path: Path) -> Path:
    """Create test data directory with scenario files."""
    data_dir = tmp_path / "data"
    scenarios_dir = data_dir / "taxonomy" / "scenarios"
    scenarios_dir.mkdir(parents=True)

    # Technology scenarios
    tech_scenarios = [
        {
            "id": "tech-saas-product-001",
            "name": "SaaS Product Development",
            "description": "Building and delivering SaaS products",
            "industry": "Technology",
            "sub_industry": "Software",
            "tags": ["product", "development", "agile"],
            "related_scenarios": ["tech-cloud-ops-001"],
            "metadata": {
                "created_at": "2025-01-20T10:00:00",
                "updated_at": "2025-01-20T10:00:00",
            },
        },
        {
            "id": "tech-cloud-ops-001",
            "name": "Cloud Operations",
            "description": "Managing cloud infrastructure",
            "industry": "Technology",
            "sub_industry": "Cloud Services",
            "tags": ["cloud", "devops", "infrastructure"],
            "related_scenarios": ["tech-saas-product-001"],
            "metadata": {
                "created_at": "2025-01-20T10:00:00",
                "updated_at": "2025-01-20T10:00:00",
            },
        },
    ]

    for scenario in tech_scenarios:
        file_path = scenarios_dir / f"{scenario['id']}.yaml"
        with open(file_path, "w", encoding="utf-8") as f:
            yaml.dump(scenario, f)

    # Finance scenarios
    finance_scenarios = [
        {
            "id": "finance-wealth-mgmt-001",
            "name": "Wealth Management",
            "description": "Personal wealth advisory services",
            "industry": "Finance",
            "sub_industry": "Wealth Management",
            "tags": ["wealth", "advisory", "investment"],
            "related_scenarios": [],
            "metadata": {
                "created_at": "2025-01-20T10:00:00",
                "updated_at": "2025-01-20T10:00:00",
            },
        },
        {
            "id": "finance-trading-ops-001",
            "name": "Trading Operations",
            "description": "Executing and managing trades",
            "industry": "Finance",
            "sub_industry": "Trading",
            "tags": ["trading", "investment", "operations"],
            "related_scenarios": ["finance-wealth-mgmt-001"],
            "metadata": {
                "created_at": "2025-01-20T10:00:00",
                "updated_at": "2025-01-20T10:00:00",
            },
        },
    ]

    for scenario in finance_scenarios:
        file_path = scenarios_dir / f"{scenario['id']}.yaml"
        with open(file_path, "w", encoding="utf-8") as f:
            yaml.dump(scenario, f)

    return data_dir


def test_initialization(scenario_data_dir: Path) -> None:
    """Test repository initialization."""
    repo = ScenarioRepository(scenario_data_dir)

    assert repo.count() == 4
    assert repo.exists("tech-saas-product-001")
    assert repo.exists("finance-wealth-mgmt-001")


def test_get_by_industry(scenario_data_dir: Path) -> None:
    """Test filtering scenarios by industry."""
    repo = ScenarioRepository(scenario_data_dir)

    tech_scenarios = repo.get_by_industry("Technology")
    assert len(tech_scenarios) == 2
    assert all(s.industry == "Technology" for s in tech_scenarios)

    finance_scenarios = repo.get_by_industry("Finance")
    assert len(finance_scenarios) == 2
    assert all(s.industry == "Finance" for s in finance_scenarios)

    no_scenarios = repo.get_by_industry("Healthcare")
    assert len(no_scenarios) == 0


def test_get_by_sub_industry(scenario_data_dir: Path) -> None:
    """Test filtering scenarios by sub-industry."""
    repo = ScenarioRepository(scenario_data_dir)

    software_scenarios = repo.get_by_sub_industry("Software")
    assert len(software_scenarios) == 1
    assert software_scenarios[0].id == "tech-saas-product-001"

    wealth_scenarios = repo.get_by_sub_industry("Wealth Management")
    assert len(wealth_scenarios) == 1
    assert wealth_scenarios[0].id == "finance-wealth-mgmt-001"


def test_get_by_tags_any(scenario_data_dir: Path) -> None:
    """Test filtering scenarios by tags (ANY match)."""
    repo = ScenarioRepository(scenario_data_dir)

    # Any scenario with "investment" tag
    investment_scenarios = repo.get_by_tags(["investment"], match_all=False)
    assert len(investment_scenarios) == 2
    ids = {s.id for s in investment_scenarios}
    assert ids == {"finance-wealth-mgmt-001", "finance-trading-ops-001"}

    # Any scenario with "cloud" OR "wealth" tags
    cloud_or_wealth = repo.get_by_tags(["cloud", "wealth"], match_all=False)
    assert len(cloud_or_wealth) == 2


def test_get_by_tags_all(scenario_data_dir: Path) -> None:
    """Test filtering scenarios by tags (ALL match)."""
    repo = ScenarioRepository(scenario_data_dir)

    # Scenarios with both "trading" AND "investment" tags
    trading_investment = repo.get_by_tags(["trading", "investment"], match_all=True)
    assert len(trading_investment) == 1
    assert trading_investment[0].id == "finance-trading-ops-001"

    # No scenario has both "cloud" AND "wealth"
    no_match = repo.get_by_tags(["cloud", "wealth"], match_all=True)
    assert len(no_match) == 0


def test_get_related_depth_1(scenario_data_dir: Path) -> None:
    """Test getting directly related scenarios."""
    repo = ScenarioRepository(scenario_data_dir)

    # tech-saas-product-001 is related to tech-cloud-ops-001
    related = repo.get_related("tech-saas-product-001", max_depth=1)
    assert related == {"tech-cloud-ops-001"}

    # tech-cloud-ops-001 is also related back
    related_back = repo.get_related("tech-cloud-ops-001", max_depth=1)
    assert related_back == {"tech-saas-product-001"}

    # finance-wealth-mgmt-001 has no related scenarios
    no_related = repo.get_related("finance-wealth-mgmt-001", max_depth=1)
    assert no_related == set()


def test_get_related_depth_2(scenario_data_dir: Path) -> None:
    """Test getting related scenarios with depth 2."""
    repo = ScenarioRepository(scenario_data_dir)

    # finance-trading-ops-001 -> finance-wealth-mgmt-001 -> (no further relations)
    related = repo.get_related("finance-trading-ops-001", max_depth=2)
    assert related == {"finance-wealth-mgmt-001"}


def test_list_industries(scenario_data_dir: Path) -> None:
    """Test listing all industries."""
    repo = ScenarioRepository(scenario_data_dir)

    industries = repo.list_industries()
    assert industries == ["Finance", "Technology"]


def test_list_sub_industries(scenario_data_dir: Path) -> None:
    """Test listing all sub-industries."""
    repo = ScenarioRepository(scenario_data_dir)

    # All sub-industries
    all_sub = repo.list_sub_industries()
    assert len(all_sub) == 4
    assert "Software" in all_sub
    assert "Wealth Management" in all_sub

    # Sub-industries for Technology
    tech_sub = repo.list_sub_industries("Technology")
    assert len(tech_sub) == 2
    assert "Software" in tech_sub
    assert "Cloud Services" in tech_sub

    # Sub-industries for Finance
    finance_sub = repo.list_sub_industries("Finance")
    assert len(finance_sub) == 2
    assert "Wealth Management" in finance_sub
    assert "Trading" in finance_sub


def test_list_tags(scenario_data_dir: Path) -> None:
    """Test listing all tags."""
    repo = ScenarioRepository(scenario_data_dir)

    tags = repo.list_tags()
    # Total unique tags across all scenarios
    assert len(tags) == 11
    assert "product" in tags
    assert "cloud" in tags
    assert "investment" in tags
    assert "advisory" in tags
    assert "wealth" in tags


def test_search(scenario_data_dir: Path) -> None:
    """Test searching scenarios by name or description."""
    repo = ScenarioRepository(scenario_data_dir)

    # Search by name
    saas_results = repo.search("SaaS")
    assert len(saas_results) == 1
    assert saas_results[0].id == "tech-saas-product-001"

    # Search by description (case-insensitive)
    wealth_results = repo.search("wealth")
    assert len(wealth_results) == 1
    assert wealth_results[0].id == "finance-wealth-mgmt-001"

    # Search matches multiple scenarios
    operations_results = repo.search("operations")
    assert len(operations_results) == 2

    # No match
    no_results = repo.search("healthcare")
    assert len(no_results) == 0
