"""Inference application models."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.inference.entities import Observation


@dataclass(frozen=True, slots=True)
class InferenceResponse:
    """Inference response."""

    observations: tuple[
        Observation,
        ...,
    ]
