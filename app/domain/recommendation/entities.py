"""Recommendation domain entities."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.inference.entities import Observation


@dataclass(frozen=True, slots=True)
class Recommendation:
    """A user-facing recommendation."""

    id: str

    title: str

    description: str

    observation: Observation
