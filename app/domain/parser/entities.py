"""Parser domain entities."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import PurePosixPath


@dataclass(frozen=True, slots=True)
class DocumentSection:
    """A logical document section."""

    heading: str
    level: int
    content: str


@dataclass(frozen=True, slots=True)
class ParsedDocument:
    """Normalized parsed repository document."""

    path: PurePosixPath
    language: str
    title: str
    plain_text: str
    sections: tuple[DocumentSection, ...] = field(default_factory=tuple)
    metadata: dict[str, str] = field(default_factory=dict)
