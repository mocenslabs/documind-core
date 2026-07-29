"""Knowledge normalization entities."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class NormalizedKnowledge:
    """Canonical knowledge representation."""

    category: str
    value: str
