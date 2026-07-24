"""Immutable repository knowledge entities."""

from dataclasses import dataclass
from pathlib import PurePosixPath


@dataclass(frozen=True, slots=True)
class Knowledge:
    """Represent normalized knowledge derived from a source path."""

    name: str
    source: PurePosixPath


@dataclass(frozen=True, slots=True)
class Technology(Knowledge):
    """Represent a detected programming technology."""


@dataclass(frozen=True, slots=True)
class Framework(Knowledge):
    """Represent a detected application framework or tool."""


@dataclass(frozen=True, slots=True)
class Container(Knowledge):
    """Represent a detected container technology."""


@dataclass(frozen=True, slots=True)
class CIPlatform(Knowledge):
    """Represent a detected continuous-integration platform."""
