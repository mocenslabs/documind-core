"""Rule domain entities."""

from collections.abc import Sequence
from dataclasses import dataclass

from app.domain.knowledge.entities import Knowledge


@dataclass(frozen=True, slots=True)
class RuleResult:
    """Represent the normalized knowledge produced by one rule."""

    knowledge: Sequence[Knowledge]
