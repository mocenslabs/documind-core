"""Repository domain entities."""

from dataclasses import dataclass
from pathlib import Path, PurePosixPath

from app.domain.repository.value_objects import RepositoryReference


@dataclass(frozen=True, slots=True)
class RepositorySnapshot:
    """Represent a loaded repository using path-only inventory data."""

    repository: RepositoryReference
    root_path: Path
    files: tuple[PurePosixPath, ...]
    directories: tuple[PurePosixPath, ...]
