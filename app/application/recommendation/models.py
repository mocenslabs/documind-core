"""Recommendation application models."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.recommendation.entities import Recommendation


@dataclass(frozen=True, slots=True)
class RecommendationResponse:
    """Recommendation response."""

    recommendations: tuple[
        Recommendation,
        ...,
    ]
