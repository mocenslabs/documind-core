"""Repository loading interfaces."""

from abc import ABC, abstractmethod

from app.domain.repository.entities import RepositorySnapshot
from app.domain.repository.value_objects import RepositorySnapshotRequest


class RepositoryLoader(ABC):
    """Define the boundary for loading repository snapshots."""

    @abstractmethod
    def load(self, request: RepositorySnapshotRequest) -> RepositorySnapshot:
        """Load a snapshot that satisfies the requested repository scope."""
