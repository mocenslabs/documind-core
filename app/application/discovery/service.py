"""Application service for snapshot discovery."""

from app.domain.discovery.facts import FoundDirectory, FoundFile, RawFact
from app.domain.discovery.interfaces import DiscoveryEngine
from app.domain.repository.entities import RepositorySnapshot


class DiscoveryService(DiscoveryEngine):
    """Produce deterministic path facts from a repository snapshot."""

    def discover(self, snapshot: RepositorySnapshot) -> list[RawFact]:
        """Return file and directory facts derived solely from the snapshot."""
        facts: list[RawFact] = [
            *(FoundFile(path) for path in snapshot.files),
            *(FoundDirectory(path) for path in snapshot.directories),
        ]
        return sorted(
            facts,
            key=lambda fact: (fact.path.as_posix(), type(fact).__name__),
        )
