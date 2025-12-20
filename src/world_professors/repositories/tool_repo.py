"""Repository for tool entities."""

from pathlib import Path

from world_professors.models.tool import Tool
from world_professors.repositories.base import BaseRepository


class ToolRepository(BaseRepository[Tool]):
    """Repository for managing tool entities."""

    def __init__(self, data_dir: Path) -> None:
        tools_dir = Path(data_dir) / "tools"
        super().__init__(tools_dir, Tool)

