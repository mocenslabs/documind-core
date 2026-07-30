"""Inference rule entities."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.inference.entities import Observation


@dataclass(frozen=True, slots=True)
class InferenceRule:
    """Single inference rule."""

    node: str
    observation: Observation
