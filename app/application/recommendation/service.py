"""Recommendation application service."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.inference.entities import Observation
from app.domain.recommendation.interfaces import RecommendationEngine

from .models import RecommendationResponse


@dataclass(frozen=True, slots=True)
class RecommendationService:
    """Coordinate recommendation generation."""

    engine: RecommendationEngine

    def recommend(
        self,
        observations: tuple[
            Observation,
            ...,
        ],
    ) -> RecommendationResponse:
        """Generate recommendations."""

        return RecommendationResponse(
            recommendations=self.engine.recommend(
                observations,
            ),
        )
