"""Application models for repository analysis."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.discovery.facts import RawFact
from app.domain.inference.entities import Observation
from app.domain.knowledge.entities import Knowledge
from app.domain.parser.entities import ParsedDocument
from app.domain.recommendation.entities import Recommendation
from app.domain.repository.entities import RepositorySnapshot
from app.domain.scanner.entities import ScanDocument


@dataclass(frozen=True, slots=True)
class AnalysisResult:
    """Aggregates the complete repository analysis."""

    repository: RepositorySnapshot

    scanned_documents: tuple[ScanDocument, ...]

    parsed_documents: tuple[ParsedDocument, ...]

    facts: list[RawFact]

    knowledge: list[Knowledge]

    observations: tuple[Observation, ...] = ()

    recommendations: tuple[Recommendation, ...] = ()
