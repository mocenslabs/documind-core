"""Application service for knowledge normalization."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.content.entities import ContentMatch
from app.domain.normalizer.interfaces import KnowledgeNormalizer

from .models import NormalizationResponse


@dataclass(frozen=True, slots=True)
class NormalizationService:
    """Coordinate knowledge normalization."""

    normalizer: KnowledgeNormalizer

    def normalize(
        self,
        matches: list[ContentMatch],
    ) -> NormalizationResponse:
        """Normalize extracted knowledge."""

        return NormalizationResponse(
            knowledge=tuple(self.normalizer.normalize(matches))
        )
