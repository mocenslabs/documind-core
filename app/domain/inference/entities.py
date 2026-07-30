"""Inference domain entities."""

from __future__ import annotations

from dataclasses import dataclass, field

from .actions import SuggestedAction
from .category import ObservationCategory
from .confidence import Confidence
from .priority import Priority
from .severity import Severity


@dataclass(frozen=True, slots=True)
class Observation:
    """Inference observation."""

    code: str

    title: str

    description: str

    category: ObservationCategory

    severity: Severity

    priority: Priority

    confidence: Confidence

    actions: tuple[SuggestedAction, ...] = field(default_factory=tuple)
