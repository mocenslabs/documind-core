"""Application models for repository loading."""

from dataclasses import dataclass

from app.domain.repository.value_objects import RepositorySnapshotRequest


@dataclass(frozen=True, slots=True)
class RepositorySnapshotRequestModel:
    """Carry a snapshot request across the application boundary."""

    request: RepositorySnapshotRequest
