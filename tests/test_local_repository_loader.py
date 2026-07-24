"""Tests for the local repository loader."""

from pathlib import Path, PurePosixPath

import pytest

from app.domain.repository.value_objects import (
    RepositoryReference,
    RepositorySnapshotRequest,
)
from app.infrastructure.repository_loader.local_loader import LocalRepositoryLoader


def test_local_repository_loader_creates_relative_path_snapshot(
    tmp_path: Path,
) -> None:
    """Load files and directories while excluding internal directories."""
    repository_path = tmp_path / "repository"
    repository_path.mkdir()
    (repository_path / "src").mkdir()
    (repository_path / "src" / "main.py").touch()
    (repository_path / "README.md").touch()
    (repository_path / ".git").mkdir()
    (repository_path / ".git" / "config").touch()
    (repository_path / "__pycache__").mkdir()
    (repository_path / "__pycache__" / "cached.pyc").touch()
    (repository_path / ".venv").mkdir()
    (repository_path / ".venv" / "pyvenv.cfg").touch()

    request = RepositorySnapshotRequest(
        repository=RepositoryReference(locator=repository_path.as_posix())
    )

    snapshot = LocalRepositoryLoader().load(request)

    assert snapshot.root_path == repository_path.resolve()
    assert snapshot.files == (
        PurePosixPath("README.md"),
        PurePosixPath("src/main.py"),
    )
    assert snapshot.directories == (PurePosixPath("src"),)


def test_local_repository_loader_rejects_missing_path(tmp_path: Path) -> None:
    """Reject a repository reference that does not exist."""
    missing_path = tmp_path / "missing"
    request = RepositorySnapshotRequest(
        repository=RepositoryReference(locator=missing_path.as_posix())
    )

    with pytest.raises(ValueError, match="does not exist"):
        LocalRepositoryLoader().load(request)
