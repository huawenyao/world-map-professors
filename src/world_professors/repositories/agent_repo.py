"""Repository for agent entities."""

from pathlib import Path

from world_professors.models.agent import Agent
from world_professors.repositories.base import BaseRepository


class AgentRepository(BaseRepository[Agent]):
    """Repository for managing agent entities."""

    def __init__(self, data_dir: Path) -> None:
        agents_dir = Path(data_dir) / "agents"
        super().__init__(agents_dir, Agent)

