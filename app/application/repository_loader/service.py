"""Application service contracts for repository loading."""

from dataclasses import dataclass

from app.domain.repository.interfaces import RepositoryLoader


@dataclass(frozen=True, slots=True)
class RepositoryLoaderService:
    """Hold the repository-loading dependency for future application use."""

    loader: RepositoryLoader
