"""Composite inference rules."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.inference.entities import Observation


@dataclass(frozen=True, slots=True)
class CompositeInferenceRule:
    """Inference rule requiring multiple nodes."""

    nodes: tuple[str, ...]

    observation: Observation
