"""Repository layer for data access."""

from pathlib import Path

from world_professors.repositories.base import (
    BaseRepository,
    EntityNotFoundError,
    RepositoryError,
    ValidationFailedError,
)
from world_professors.repositories.capability_repo import CapabilityRepository
from world_professors.repositories.industry_repo import IndustryRepository
from world_professors.repositories.role_repo import RoleRepository
from world_professors.repositories.scenario_repo import ScenarioRepository
from world_professors.repositories.agent_repo import AgentRepository
from world_professors.repositories.tool_repo import ToolRepository
from world_professors.repositories.workflow_repo import WorkflowRepository

__all__ = [
    "BaseRepository",
    "RepositoryError",
    "EntityNotFoundError",
    "ValidationFailedError",
    "ScenarioRepository",
    "RoleRepository",
    "CapabilityRepository",
    "IndustryRepository",
    "WorkflowRepository",
    "AgentRepository",
    "ToolRepository",
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
        self._industries: IndustryRepository | None = None
        self._workflows: WorkflowRepository | None = None
        self._agents: AgentRepository | None = None
        self._tools: ToolRepository | None = None

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

    @property
    def industries(self) -> IndustryRepository:
        """Get industry repository (lazy-loaded singleton)."""
        if self._industries is None:
            self._industries = IndustryRepository(self.data_dir)
        return self._industries

    @property
    def workflows(self) -> WorkflowRepository:
        """Get workflow repository (lazy-loaded singleton)."""
        if self._workflows is None:
            self._workflows = WorkflowRepository(self.data_dir)
        return self._workflows

    @property
    def agents(self) -> AgentRepository:
        """Get agent repository (lazy-loaded singleton)."""
        if self._agents is None:
            self._agents = AgentRepository(self.data_dir)
        return self._agents

    @property
    def tools(self) -> ToolRepository:
        """Get tool repository (lazy-loaded singleton)."""
        if self._tools is None:
            self._tools = ToolRepository(self.data_dir)
        return self._tools

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
        if self._industries is not None:
            self._industries.refresh()
        if self._workflows is not None:
            self._workflows.refresh()
        if self._agents is not None:
            self._agents.refresh()
        if self._tools is not None:
            self._tools.refresh()
