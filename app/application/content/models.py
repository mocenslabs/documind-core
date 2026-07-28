"""Application models for content discovery."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.content.entities import ContentMatch


@dataclass(frozen=True, slots=True)
class ContentDiscoveryResponse:
    """Application response."""

    matches: tuple[ContentMatch, ...]
