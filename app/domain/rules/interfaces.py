"""Generic rule interfaces."""

from abc import ABC, abstractmethod
from collections.abc import Sequence

from app.domain.discovery.facts import RawFact
from app.domain.knowledge.entities import Knowledge


class Rule(ABC):
    """Define a source-independent normalization rule."""

    @abstractmethod
    def apply(self, facts: Sequence[RawFact]) -> list[Knowledge]:
        """Produce knowledge entities from the supplied raw facts."""
