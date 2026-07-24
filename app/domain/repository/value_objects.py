"""Immutable value objects for repository loading."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RepositoryReference:
    """Identify a repository source and its optional revision."""

    locator: str
    revision: str | None = None


@dataclass(frozen=True, slots=True)
class RepositorySnapshotRequest:
    """Describe the repository material requested for a snapshot."""

    repository: RepositoryReference
    included_paths: tuple[str, ...] = ()
    excluded_paths: tuple[str, ...] = ()
