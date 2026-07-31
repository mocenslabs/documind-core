"""Recommendation rule engine."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.inference.entities import Observation
from app.domain.recommendation.entities import Recommendation


@dataclass(frozen=True, slots=True)
class RecommendationRuleEngine:
    """Convert observations into recommendations."""

    def build(
        self,
        observations: tuple[
            Observation,
            ...,
        ],
    ) -> tuple[
        Recommendation,
        ...,
    ]:
        """Build recommendations."""

        recommendations: list[Recommendation] = []

        for observation in observations:
            recommendations.append(
                Recommendation(
                    id=observation.code,
                    title=observation.title,
                    description=observation.description,
                    observation=observation,
                )
            )

        return tuple(recommendations)
