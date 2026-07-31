"""Recommendation domain contracts."""

from __future__ import annotations

from abc import ABC, abstractmethod

from app.domain.inference.entities import Observation

from .entities import Recommendation


class RecommendationEngine(ABC):
    """Build recommendations from observations."""

    @abstractmethod
    def recommend(
        self,
        observations: tuple[Observation, ...],
    ) -> tuple[Recommendation, ...]:
        """Create recommendations."""
