"""Knowledge production interfaces."""

from abc import ABC, abstractmethod
from collections.abc import Sequence

from app.domain.discovery.facts import RawFact
from app.domain.knowledge.entities import Knowledge


class KnowledgeEngine(ABC):
    """Define the boundary for producing repository knowledge."""

    @abstractmethod
    def build(self, facts: Sequence[RawFact]) -> list[Knowledge]:
        """Build normalized knowledge from the supplied raw facts."""
