"""Application service for repository knowledge."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from app.application.knowledge.classification import CandidateClassifier
from app.application.knowledge.deduplication import CandidateDeduplicator
from app.application.knowledge.models import (
    ClassifiedKnowledgeResponse,
    KnowledgeExtractionResponse,
)
from app.application.rules.service import RuleEngineService
from app.domain.discovery.facts import RawFact
from app.domain.knowledge.entities import Knowledge, KnowledgeCandidate
from app.domain.knowledge.interfaces import KnowledgeEngine, KnowledgeExtractor
from app.domain.parser.entities import ParsedDocument


@dataclass(frozen=True, slots=True)
class KnowledgeService(KnowledgeEngine):
    """Produce repository knowledge through the configured rule engine."""

    rule_engine: RuleEngineService

    def build(self, facts: Sequence[RawFact]) -> list[Knowledge]:
        """Build normalized knowledge from the supplied raw facts."""
        return self.rule_engine.evaluate(facts)


@dataclass(frozen=True, slots=True)
class KnowledgeExtractionService:
    """Coordinate repository knowledge extraction."""

    extractor: KnowledgeExtractor
    deduplicator: CandidateDeduplicator = CandidateDeduplicator()

    def extract(
        self,
        documents: tuple[ParsedDocument, ...],
    ) -> KnowledgeExtractionResponse:
        """Extract raw knowledge."""

        candidates = self.extractor.extract(documents)

        unique = self.deduplicator.deduplicate(
            tuple(candidates),
        )

        return KnowledgeExtractionResponse(
            candidates=unique,
        )


@dataclass(frozen=True, slots=True)
class KnowledgeClassificationService:
    """Classify extracted knowledge."""

    classifier: CandidateClassifier

    def classify(
        self,
        candidates: tuple[KnowledgeCandidate, ...],
    ) -> ClassifiedKnowledgeResponse:
        return ClassifiedKnowledgeResponse(
            categories=self.classifier.classify(
                candidates,
            ),
        )
