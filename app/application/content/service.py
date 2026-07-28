"""Application service for content discovery."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.content.interfaces import ContentDiscoveryEngine
from app.domain.parser.entities import ParsedDocument

from .models import ContentDiscoveryResponse


@dataclass(frozen=True, slots=True)
class ContentDiscoveryService:
    """Coordinate structured content extraction."""

    engine: ContentDiscoveryEngine

    def discover(
        self,
        documents: tuple[ParsedDocument, ...],
    ) -> ContentDiscoveryResponse:
        """Execute structured discovery."""

        return ContentDiscoveryResponse(matches=tuple(self.engine.discover(documents)))
