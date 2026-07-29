"""Application models for repository parsing."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.parser.entities import ParsedDocument


@dataclass(frozen=True, slots=True)
class ParseResponse:
    """Application response for parsed documents."""

    documents: tuple[ParsedDocument, ...]
