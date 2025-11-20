"""Base repository for data access layer."""

from pathlib import Path
from typing import Generic, TypeVar

import yaml
from pydantic import ValidationError

from world_professors.models.base import BaseEntity

# Generic type variable for entity models
T = TypeVar("T", bound=BaseEntity)


class RepositoryError(Exception):
    """Base exception for repository operations."""

    pass


class EntityNotFoundError(RepositoryError):
    """Raised when an entity is not found."""

    def __init__(self, entity_id: str, entity_type: str) -> None:
        """Initialize error with entity details."""
        self.entity_id = entity_id
        self.entity_type = entity_type
        super().__init__(f"{entity_type} with ID '{entity_id}' not found")


class ValidationFailedError(RepositoryError):
    """Raised when entity validation fails."""

    def __init__(self, file_path: Path, errors: list[dict[str, object]]) -> None:
        """Initialize error with validation details."""
        self.file_path = file_path
        self.errors = errors
        error_summary = "; ".join([f"{e['loc']}: {e['msg']}" for e in errors])
        super().__init__(f"Validation failed for {file_path}: {error_summary}")


class BaseRepository(Generic[T]):
    """Generic base repository for entity CRUD operations.

    Type Parameters:
        T: Entity model class (must inherit from BaseEntity)

    Attributes:
        data_dir: Root directory for data files
        model_class: Pydantic model class for entity type
        _index: In-memory index mapping entity IDs to file paths
    """

    def __init__(self, data_dir: Path, model_class: type[T]) -> None:
        """Initialize repository.

        Args:
            data_dir: Root directory containing data files
            model_class: Pydantic model class for this entity type
        """
        self.data_dir = Path(data_dir)
        self.model_class = model_class
        self._index: dict[str, Path] = {}

        # Build index on initialization
        self._build_index()

    def _build_index(self) -> None:
        """Build in-memory index of entity IDs to file paths.

        Scans all YAML files in data_dir and its subdirectories.
        Subclasses should override to specify custom search paths.
        """
        if not self.data_dir.exists():
            return

        for yaml_file in self.data_dir.rglob("*.yaml"):
            try:
                entity = self.load(yaml_file)
                self._index[entity.id] = yaml_file
            except (ValidationFailedError, ValidationError, yaml.YAMLError, KeyError):
                # Skip invalid files during index building
                continue

    def load(self, file_path: Path) -> T:
        """Load and validate entity from YAML file.

        Args:
            file_path: Path to YAML file

        Returns:
            Validated entity instance

        Raises:
            FileNotFoundError: If file doesn't exist
            ValidationFailedError: If validation fails
            yaml.YAMLError: If YAML parsing fails
        """
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)

        try:
            return self.model_class.model_validate(data)
        except ValidationError as e:
            raise ValidationFailedError(file_path, e.errors())  # type: ignore[arg-type]

    def load_all(self) -> list[T]:
        """Load all entities from indexed files.

        Returns:
            List of all valid entities

        Note:
            Silently skips files that fail validation.
        """
        entities = []
        for file_path in self._index.values():
            try:
                entity = self.load(file_path)
                entities.append(entity)
            except (ValidationError, yaml.YAMLError):
                continue

        return entities

    def get_by_id(self, entity_id: str) -> T:
        """Get entity by ID.

        Args:
            entity_id: Unique entity identifier

        Returns:
            Entity instance

        Raises:
            EntityNotFoundError: If entity with given ID doesn't exist
        """
        if entity_id not in self._index:
            raise EntityNotFoundError(entity_id, self.model_class.__name__)

        file_path = self._index[entity_id]
        return self.load(file_path)

    def save(self, entity: T, file_path: Path | None = None) -> Path:
        """Save entity to YAML file.

        Args:
            entity: Entity instance to save
            file_path: Target file path (optional, uses indexed path if exists)

        Returns:
            Path where entity was saved

        Raises:
            ValueError: If file_path is None and entity not in index
        """
        # Determine target file path
        if file_path is None:
            if entity.id not in self._index:
                raise ValueError(
                    f"Cannot save new entity without file_path: {entity.id}"
                )
            file_path = self._index[entity.id]

        # Ensure parent directory exists
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Write YAML file
        yaml_content = entity.to_yaml()
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(yaml_content)

        # Update index
        self._index[entity.id] = file_path

        return file_path

    def delete(self, entity_id: str) -> None:
        """Delete entity by ID.

        Args:
            entity_id: ID of entity to delete

        Raises:
            EntityNotFoundError: If entity doesn't exist
        """
        if entity_id not in self._index:
            raise EntityNotFoundError(entity_id, self.model_class.__name__)

        file_path = self._index[entity_id]
        file_path.unlink()
        del self._index[entity_id]

    def exists(self, entity_id: str) -> bool:
        """Check if entity exists.

        Args:
            entity_id: Entity ID to check

        Returns:
            True if entity exists, False otherwise
        """
        return entity_id in self._index

    def count(self) -> int:
        """Count total number of entities.

        Returns:
            Number of entities in repository
        """
        return len(self._index)

    def refresh(self) -> None:
        """Refresh index by rescanning data directory.

        Useful when files are added/modified externally.
        """
        self._index.clear()
        self._build_index()
