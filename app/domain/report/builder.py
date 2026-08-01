"""Report builder."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.inference.entities import Observation
from app.domain.knowledge.entities import Knowledge
from app.domain.recommendation.entities import Recommendation

from .entities import RepositoryReport


@dataclass(frozen=True, slots=True)
class RepositoryReportBuilder:
    """Build repository reports."""

    def build(
        self,
        *,
        knowledge: tuple[
            Knowledge,
            ...,
        ],
        observations: tuple[
            Observation,
            ...,
        ],
        recommendations: tuple[
            Recommendation,
            ...,
        ],
    ) -> RepositoryReport:
        """Create a repository report."""

        return RepositoryReport(
            knowledge=knowledge,
            observations=observations,
            recommendations=recommendations,
        )
