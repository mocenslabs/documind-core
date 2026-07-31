"""Local recommendation engine."""

from __future__ import annotations

from app.application.recommendation.rule_engine import (
    RecommendationRuleEngine,
)
from app.domain.inference.entities import Observation
from app.domain.recommendation.entities import Recommendation
from app.domain.recommendation.interfaces import RecommendationEngine


class LocalRecommendationEngine(RecommendationEngine):
    """Generate recommendations."""

    def __init__(
        self,
    ) -> None:
        self._engine = RecommendationRuleEngine()

    def recommend(
        self,
        observations: tuple[
            Observation,
            ...,
        ],
    ) -> tuple[
        Recommendation,
        ...,
    ]:
        """Generate recommendations."""

        return self._engine.build(
            observations,
        )
