"""Discovery engine interfaces."""

from abc import ABC, abstractmethod

from app.domain.discovery.facts import RawFact
from app.domain.repository.entities import RepositorySnapshot


class DiscoveryEngine(ABC):
    """Define the boundary for discovering raw repository facts."""

    @abstractmethod
    def discover(self, snapshot: RepositorySnapshot) -> list[RawFact]:
        """Produce raw facts from the supplied repository snapshot."""
