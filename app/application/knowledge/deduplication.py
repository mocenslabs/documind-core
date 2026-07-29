"""Knowledge candidate deduplication."""

from __future__ import annotations

from app.domain.knowledge.entities import KnowledgeCandidate


class CandidateDeduplicator:
    """Remove duplicated knowledge candidates."""

    def deduplicate(
        self,
        candidates: tuple[KnowledgeCandidate, ...],
    ) -> tuple[KnowledgeCandidate, ...]:
        unique: dict[
            tuple[str, str],
            KnowledgeCandidate,
        ] = {}

        for candidate in candidates:
            key = (
                candidate.category,
                candidate.value.lower(),
            )

            if key not in unique:
                unique[key] = candidate

        return tuple(unique.values())
