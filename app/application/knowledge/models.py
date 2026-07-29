"""Knowledge extraction application models."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.knowledge.entities import KnowledgeCandidate


@dataclass(frozen=True, slots=True)
class KnowledgeExtractionResponse:
    """Application response for extracted knowledge."""

    candidates: tuple[KnowledgeCandidate, ...]


@dataclass(frozen=True, slots=True)
class ClassifiedKnowledgeResponse:
    """Grouped knowledge candidates."""

    categories: dict[
        str,
        tuple[KnowledgeCandidate, ...],
    ]
