"""Scanner domain entities."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import PurePosixPath


@dataclass(frozen=True, slots=True)
class ScanDocument:
    """Represents a scanned repository document."""

    path: PurePosixPath
    content: str


@dataclass(frozen=True, slots=True)
class ScanResult:
    """Collection of scanned documents."""

    documents: tuple[ScanDocument, ...]
