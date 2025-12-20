"""Repository for capability entities."""

from pathlib import Path

from world_professors.models.capability import Capability, CapabilityCategory
from world_professors.repositories.base import BaseRepository


class CapabilityRepository(BaseRepository[Capability]):
    """Repository for managing capability entities.

    Provides specialized query methods for capabilities including
    filtering by category, searching related capabilities, and prerequisite trees.
    """

    def __init__(self, data_dir: Path) -> None:
        """Initialize capability repository.

        Args:
            data_dir: Root data directory (expects capabilities in capabilities/core-skills/)
        """
        # Prefer current layout: data/capabilities/**.yaml
        # Backward compatible with legacy layout: data/capabilities/core-skills/**.yaml
        primary_dir = data_dir / "capabilities"
        legacy_dir = data_dir / "capabilities" / "core-skills"
        capabilities_dir = primary_dir if primary_dir.exists() else legacy_dir
        super().__init__(capabilities_dir, Capability)

    def get_by_category(self, category: CapabilityCategory) -> list[Capability]:
        """Get all capabilities in a specific category.

        Args:
            category: Capability category enum value

        Returns:
            List of capabilities in the category
        """
        return [c for c in self.load_all() if c.category == category]

    def get_by_sub_category(self, sub_category: str) -> list[Capability]:
        """Get all capabilities in a specific sub-category.

        Args:
            sub_category: Sub-category name

        Returns:
            List of capabilities in the sub-category
        """
        return [c for c in self.load_all() if c.sub_category == sub_category]

    def get_related(self, capability_id: str) -> list[Capability]:
        """Get capabilities related to a specific capability.

        Args:
            capability_id: Capability ID

        Returns:
            List of related capabilities

        Raises:
            EntityNotFoundError: If capability doesn't exist
        """
        capability = self.get_by_id(capability_id)
        related_capabilities = []

        for related_id in capability.related_capabilities:
            try:
                related_cap = self.get_by_id(related_id)
                related_capabilities.append(related_cap)
            except Exception:
                # Skip if related capability doesn't exist
                continue

        return related_capabilities

    def get_prerequisites(self, capability_id: str) -> list[Capability]:
        """Get prerequisite capabilities for a specific capability.

        Args:
            capability_id: Capability ID

        Returns:
            List of prerequisite capabilities (empty if no learning path defined)

        Raises:
            EntityNotFoundError: If capability doesn't exist
        """
        capability = self.get_by_id(capability_id)

        if not capability.learning_path:
            return []

        prerequisites = []
        for prereq_id in capability.learning_path.prerequisites:
            try:
                prereq_cap = self.get_by_id(prereq_id)
                prerequisites.append(prereq_cap)
            except Exception:
                # Skip if prerequisite doesn't exist
                continue

        return prerequisites

    def get_prerequisite_chain(self, capability_id: str) -> list[str]:
        """Get full prerequisite chain (transitive closure).

        Args:
            capability_id: Starting capability ID

        Returns:
            List of capability IDs in prerequisite order (root to leaf)

        Raises:
            EntityNotFoundError: If capability doesn't exist
        """
        visited = set()
        chain = []

        def visit(cap_id: str) -> None:
            if cap_id in visited:
                return

            visited.add(cap_id)

            try:
                prerequisites = self.get_prerequisites(cap_id)
                for prereq in prerequisites:
                    visit(prereq.id)

                chain.append(cap_id)
            except Exception:
                pass

        visit(capability_id)
        return chain

    def get_capabilities_by_level(self) -> dict[str, list[Capability]]:
        """Group capabilities by their defined levels.

        Returns:
            Dictionary mapping level names to lists of capabilities
        """
        by_level: dict[str, list[Capability]] = {}

        for capability in self.load_all():
            for level in capability.levels.keys():
                if level not in by_level:
                    by_level[level] = []
                by_level[level].append(capability)

        return by_level

    def list_categories(self) -> list[CapabilityCategory]:
        """Get list of all categories with capabilities.

        Returns:
            List of category enum values
        """
        categories = {c.category for c in self.load_all()}
        return sorted(categories, key=lambda x: x.value)

    def list_sub_categories(
        self, category: CapabilityCategory | None = None
    ) -> list[str]:
        """Get list of all sub-categories.

        Args:
            category: If specified, only return sub-categories for this category

        Returns:
            Sorted list of unique sub-category names (excluding None)
        """
        capabilities = self.load_all()

        if category:
            capabilities = [c for c in capabilities if c.category == category]

        sub_categories = {
            c.sub_category for c in capabilities if c.sub_category is not None
        }
        return sorted(sub_categories)

    def search(self, query: str) -> list[Capability]:
        """Search capabilities by name or description.

        Args:
            query: Search query (case-insensitive)

        Returns:
            List of matching capabilities
        """
        query_lower = query.lower()
        return [
            c
            for c in self.load_all()
            if query_lower in c.name.lower() or query_lower in c.description.lower()
        ]

    def get_capabilities_with_learning_paths(self) -> list[Capability]:
        """Get all capabilities that have learning paths defined.

        Returns:
            List of capabilities with learning paths
        """
        return [c for c in self.load_all() if c.has_learning_path]
