"""Raw facts discovered from repository snapshots."""

from dataclasses import dataclass
from pathlib import PurePosixPath


@dataclass(frozen=True, slots=True)
class RawFact:
    """Represent a direct, path-based repository observation."""

    path: PurePosixPath


@dataclass(frozen=True, slots=True)
class FoundFile(RawFact):
    """Represent a file observed in a repository snapshot."""


@dataclass(frozen=True, slots=True)
class FoundDirectory(RawFact):
    """Represent a directory observed in a repository snapshot."""
