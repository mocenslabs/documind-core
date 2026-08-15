"""Application service for snapshot discovery."""

from pathlib import PurePosixPath

from app.domain.discovery.facts import FoundDirectory, FoundFile, RawFact
from app.domain.discovery.interfaces import DiscoveryEngine
from app.domain.repository.entities import RepositorySnapshot


class DiscoveryService(DiscoveryEngine):
    """Produce deterministic path facts while ignoring generated directories."""

    EXCLUDED_DIRS: frozenset[str] = frozenset(
        {
            ".git",
            ".venv",
            "venv",
            "env",
            "node_modules",
            "__pycache__",
            "dist",
            "build",
        }
    )

    @classmethod
    def _is_excluded(cls, path: PurePosixPath) -> bool:
        """Return whether any path component belongs to an excluded directory."""
        return any(part in cls.EXCLUDED_DIRS for part in path.parts)

    def discover(self, snapshot: RepositorySnapshot) -> list[RawFact]:
        """Return deterministic facts while filtering excluded paths."""
        facts: list[RawFact] = [
            *(
                FoundFile(path)
                for path in snapshot.files
                if not self._is_excluded(path)
            ),
            *(
                FoundDirectory(path)
                for path in snapshot.directories
                if not self._is_excluded(path)
            ),
        ]

        return sorted(
            facts,
            key=lambda fact: (fact.path.as_posix(), type(fact).__name__),
        )
