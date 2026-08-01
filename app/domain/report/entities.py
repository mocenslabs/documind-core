"""Report domain entities."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.inference.entities import Observation
from app.domain.knowledge.entities import Knowledge
from app.domain.recommendation.entities import Recommendation


@dataclass(frozen=True, slots=True)
class RepositoryReport:
    """Complete repository report."""

    knowledge: tuple[
        Knowledge,
        ...,
    ]

    observations: tuple[
        Observation,
        ...,
    ]

    recommendations: tuple[
        Recommendation,
        ...,
    ]
