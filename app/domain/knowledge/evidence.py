"""Knowledge evidence domain entities."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import PurePosixPath


@dataclass(frozen=True, slots=True)
class KnowledgeEvidence:
    """Evidence supporting a knowledge item."""

    source: PurePosixPath
    kind: str
    value: str
