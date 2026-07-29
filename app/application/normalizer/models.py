"""Application models for knowledge normalization."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.normalizer.entities import NormalizedKnowledge


@dataclass(frozen=True, slots=True)
class NormalizationResponse:
    """Normalized knowledge."""

    knowledge: tuple[NormalizedKnowledge, ...]
