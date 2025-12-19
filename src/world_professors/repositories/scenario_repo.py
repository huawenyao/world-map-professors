"""Repository for scenario entities."""

from pathlib import Path

from world_professors.models.taxonomy import Scenario
from world_professors.repositories.base import BaseRepository


class ScenarioRepository(BaseRepository[Scenario]):
    """Repository for managing scenario entities.

    Provides specialized query methods for scenarios including
    filtering by industry, tags, and related scenarios.
    """

    def __init__(self, data_dir: Path) -> None:
        """Initialize scenario repository.

        Args:
            data_dir: Root data directory (expects scenarios in taxonomy/scenarios/)
        """
        # Prefer current layout: data/scenarios/**.yaml
        # Backward compatible with legacy layout: data/taxonomy/scenarios/**.yaml
        primary_dir = data_dir / "scenarios"
        legacy_dir = data_dir / "taxonomy" / "scenarios"
        scenarios_dir = primary_dir if primary_dir.exists() else legacy_dir
        super().__init__(scenarios_dir, Scenario)

    def get_by_industry(self, industry: str) -> list[Scenario]:
        """Get all scenarios for a specific industry.

        Args:
            industry: Industry name (case-sensitive)

        Returns:
            List of scenarios in the industry
        """
        return [s for s in self.load_all() if s.industry == industry]

    def get_by_sub_industry(self, sub_industry: str) -> list[Scenario]:
        """Get all scenarios for a specific sub-industry.

        Args:
            sub_industry: Sub-industry name (case-sensitive)

        Returns:
            List of scenarios in the sub-industry
        """
        return [
            s for s in self.load_all() if s.sub_industry == sub_industry
        ]

    def get_by_tags(self, tags: list[str], match_all: bool = False) -> list[Scenario]:
        """Get scenarios matching specified tags.

        Args:
            tags: List of tags to match
            match_all: If True, scenario must have ALL tags; if False, ANY tag

        Returns:
            List of matching scenarios
        """
        scenarios = self.load_all()

        if match_all:
            # Scenario must have all specified tags
            return [
                s for s in scenarios if all(tag in s.tags for tag in tags)
            ]
        else:
            # Scenario must have at least one tag
            return [
                s for s in scenarios if any(tag in s.tags for tag in tags)
            ]

    def get_related(self, scenario_id: str, max_depth: int = 1) -> set[str]:
        """Get related scenario IDs up to specified depth.

        Args:
            scenario_id: Starting scenario ID
            max_depth: Maximum traversal depth (default: 1 = direct relations)

        Returns:
            Set of related scenario IDs (excluding the starting scenario)

        Raises:
            EntityNotFoundError: If starting scenario doesn't exist
        """
        if max_depth < 1:
            return set()

        scenario = self.get_by_id(scenario_id)
        related = set(scenario.related_scenarios)

        if max_depth > 1:
            # Recursively find related scenarios
            for related_id in list(related):
                try:
                    deeper_related = self.get_related(related_id, max_depth - 1)
                    related.update(deeper_related)
                except Exception:
                    # Skip if related scenario doesn't exist
                    continue

            # Remove the starting scenario from results
            related.discard(scenario_id)

        return related

    def list_industries(self) -> list[str]:
        """Get list of all industries with scenarios.

        Returns:
            Sorted list of unique industry names
        """
        industries = {s.industry for s in self.load_all()}
        return sorted(industries)

    def list_sub_industries(self, industry: str | None = None) -> list[str]:
        """Get list of all sub-industries.

        Args:
            industry: If specified, only return sub-industries for this industry

        Returns:
            Sorted list of unique sub-industry names (excluding None)
        """
        scenarios = self.load_all()

        if industry:
            scenarios = [s for s in scenarios if s.industry == industry]

        sub_industries = {
            s.sub_industry for s in scenarios if s.sub_industry is not None
        }
        return sorted(sub_industries)

    def list_tags(self) -> list[str]:
        """Get list of all tags used across scenarios.

        Returns:
            Sorted list of unique tags
        """
        all_tags = set()
        for scenario in self.load_all():
            all_tags.update(scenario.tags)

        return sorted(all_tags)

    def search(self, query: str) -> list[Scenario]:
        """Search scenarios by name or description.

        Args:
            query: Search query (case-insensitive)

        Returns:
            List of matching scenarios
        """
        query_lower = query.lower()
        return [
            s
            for s in self.load_all()
            if query_lower in s.name.lower()
            or query_lower in s.description.lower()
        ]
