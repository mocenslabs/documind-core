"""Application models for repository analysis."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.discovery.facts import RawFact
from app.domain.knowledge.entities import Knowledge
from app.domain.repository.entities import RepositorySnapshot
from app.domain.scanner.entities import ScanDocument


@dataclass(frozen=True, slots=True)
class AnalysisResult:
    """Aggregates the complete repository analysis."""

    repository: RepositorySnapshot

    scanned_documents: tuple[ScanDocument, ...]

    facts: list[RawFact]

    knowledge: list[Knowledge]
