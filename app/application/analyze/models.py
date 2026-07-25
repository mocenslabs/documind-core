"""Application models for repository analysis."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.discovery.facts import RawFact
from app.domain.knowledge.entities import Knowledge
from app.domain.repository.entities import RepositorySnapshot


@dataclass(frozen=True, slots=True)
class AnalysisResult:
    """Result of the repository analysis pipeline."""

    repository: RepositorySnapshot
    facts: list[RawFact]
    knowledge: list[Knowledge]
