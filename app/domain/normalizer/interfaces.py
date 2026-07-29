"""Knowledge normalization contracts."""

from __future__ import annotations

from abc import ABC, abstractmethod

from app.domain.content.entities import ContentMatch

from .entities import NormalizedKnowledge


class KnowledgeNormalizer(ABC):
    """Normalize extracted knowledge."""

    @abstractmethod
    def normalize(
        self,
        matches: list[ContentMatch],
    ) -> list[NormalizedKnowledge]:
        """Normalize extracted knowledge."""
