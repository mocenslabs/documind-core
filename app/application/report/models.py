"""Repository report models."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.knowledge.entities import Knowledge
from app.domain.repository.entities import RepositorySnapshot


@dataclass(slots=True)
class RepositoryStatistics:
    """Repository statistics."""

    total_files: int
    python_files: int
    markdown_files: int
    test_files: int


@dataclass(slots=True)
class RepositoryReport:
    """Human-readable repository report."""

    repository: RepositorySnapshot
    statistics: RepositoryStatistics
    knowledge: list[Knowledge]
    summary: str
