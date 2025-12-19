"""Repository for industry entities."""

from pathlib import Path

from world_professors.models.industry import Industry
from world_professors.repositories.base import BaseRepository


class IndustryRepository(BaseRepository[Industry]):
    """Repository for managing industry entities."""

    def __init__(self, data_dir: Path) -> None:
        industries_dir = Path(data_dir) / "industries"
        super().__init__(industries_dir, Industry)

