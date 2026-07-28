"""Content discovery contracts."""

from __future__ import annotations

from abc import ABC, abstractmethod

from app.domain.parser.entities import ParsedDocument

from .entities import ContentMatch


class ContentDiscoveryEngine(ABC):
    """Extract structured information from parsed documents."""

    @abstractmethod
    def discover(
        self,
        documents: tuple[ParsedDocument, ...],
    ) -> list[ContentMatch]:
        """Extract structured content."""
