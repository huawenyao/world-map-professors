"""Repository for workflow entities."""

from pathlib import Path

from world_professors.models.workflow import Workflow
from world_professors.repositories.base import BaseRepository


class WorkflowRepository(BaseRepository[Workflow]):
    """Repository for managing workflow entities."""

    def __init__(self, data_dir: Path) -> None:
        workflows_dir = Path(data_dir) / "workflows"
        super().__init__(workflows_dir, Workflow)

