"""Content discovery entities."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.parser.entities import ParsedDocument


@dataclass(frozen=True, slots=True)
class ContentMatch:
    """A piece of extracted information."""

    category: str
    value: str
    source: ParsedDocument
