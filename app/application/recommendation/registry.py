"""Recommendation registry."""

from __future__ import annotations

from dataclasses import dataclass, field

from app.domain.recommendation.entities import Recommendation


@dataclass(slots=True)
class RecommendationRegistry:
    """Store generated recommendations."""

    _recommendations: list[Recommendation] = field(
        default_factory=list,
    )

    def add(
        self,
        recommendation: Recommendation,
    ) -> None:
        """Register a recommendation."""

        self._recommendations.append(
            recommendation,
        )

    def extend(
        self,
        recommendations: tuple[
            Recommendation,
            ...,
        ],
    ) -> None:
        """Register many recommendations."""

        self._recommendations.extend(
            recommendations,
        )

    def all(
        self,
    ) -> tuple[
        Recommendation,
        ...,
    ]:
        """Return registered recommendations."""

        return tuple(
            self._recommendations,
        )

    def clear(
        self,
    ) -> None:
        """Clear registry."""

        self._recommendations.clear()
