"""Repository layer for data access."""

from pathlib import Path

from world_professors.repositories.base import (
    BaseRepository,
    EntityNotFoundError,
    RepositoryError,
    ValidationFailedError,
)
from world_professors.repositories.capability_repo import CapabilityRepository
from world_professors.repositories.role_repo import RoleRepository
from world_professors.repositories.scenario_repo import ScenarioRepository

__all__ = [
    "BaseRepository",
    "RepositoryError",
    "EntityNotFoundError",
    "ValidationFailedError",
    "ScenarioRepository",
    "RoleRepository",
    "CapabilityRepository",
    "RepositoryFactory",
]


class RepositoryFactory:
    """Factory for creating and managing repository instances.

    Provides lazy-loaded singleton instances of all repositories.
    This ensures consistent data access throughout the application.

    Example:
        factory = RepositoryFactory(Path("data"))
        scenarios = factory.scenarios.load_all()
        role = factory.roles.get_by_id("tech-saas-ai-enhanced-pm")
    """

    def __init__(self, data_dir: Path) -> None:
        """Initialize factory with data directory.

        Args:
            data_dir: Root data directory containing all entity subdirectories
        """
        self.data_dir = Path(data_dir)
        self._scenarios: ScenarioRepository | None = None
        self._roles: RoleRepository | None = None
        self._capabilities: CapabilityRepository | None = None

    @property
    def scenarios(self) -> ScenarioRepository:
        """Get scenario repository (lazy-loaded singleton).

        Returns:
            ScenarioRepository instance
        """
        if self._scenarios is None:
            self._scenarios = ScenarioRepository(self.data_dir)
        return self._scenarios

    @property
    def roles(self) -> RoleRepository:
        """Get role repository (lazy-loaded singleton).

        Returns:
            RoleRepository instance
        """
        if self._roles is None:
            self._roles = RoleRepository(self.data_dir)
        return self._roles

    @property
    def capabilities(self) -> CapabilityRepository:
        """Get capability repository (lazy-loaded singleton).

        Returns:
            CapabilityRepository instance
        """
        if self._capabilities is None:
            self._capabilities = CapabilityRepository(self.data_dir)
        return self._capabilities

    def refresh_all(self) -> None:
        """Refresh indices for all loaded repositories.

        Useful when data files are modified externally.
        """
        if self._scenarios is not None:
            self._scenarios.refresh()
        if self._roles is not None:
            self._roles.refresh()
        if self._capabilities is not None:
            self._capabilities.refresh()
