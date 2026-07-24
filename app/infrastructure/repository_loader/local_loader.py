"""Local filesystem repository loader."""

from pathlib import Path, PurePosixPath

from app.domain.repository.entities import RepositorySnapshot
from app.domain.repository.interfaces import RepositoryLoader
from app.domain.repository.value_objects import RepositorySnapshotRequest

_IGNORED_DIRECTORY_NAMES = frozenset({".git", "__pycache__", ".venv"})


class LocalRepositoryLoader(RepositoryLoader):
    """Load a local repository into a path-only snapshot."""

    def load(self, request: RepositorySnapshotRequest) -> RepositorySnapshot:
        """Load the requested local repository without reading file contents."""
        root_path = Path(request.repository.locator).resolve()

        if not root_path.exists():
            message = f"Repository path does not exist: {root_path}"
            raise ValueError(message)

        if not root_path.is_dir():
            message = f"Repository path is not a directory: {root_path}"
            raise ValueError(message)

        files: list[PurePosixPath] = []
        directories: list[PurePosixPath] = []

        for current_path, directory_names, file_names in root_path.walk():
            directory_names[:] = sorted(
                name for name in directory_names if name not in _IGNORED_DIRECTORY_NAMES
            )

            for directory_name in directory_names:
                directory_path = current_path / directory_name
                directories.append(_relative_posix_path(directory_path, root_path))

            for file_name in sorted(file_names):
                file_path = current_path / file_name
                files.append(_relative_posix_path(file_path, root_path))

        return RepositorySnapshot(
            repository=request.repository,
            root_path=root_path,
            files=tuple(files),
            directories=tuple(directories),
        )


def _relative_posix_path(path: Path, root_path: Path) -> PurePosixPath:
    """Return a repository-relative path with POSIX semantics."""
    return PurePosixPath(path.relative_to(root_path).as_posix())
