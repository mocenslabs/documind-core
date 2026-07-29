"""Knowledge candidate classification."""

from __future__ import annotations

from collections import defaultdict

from app.domain.knowledge.entities import KnowledgeCandidate


class CandidateClassifier:
    """Group candidates by category."""

    def classify(
        self,
        candidates: tuple[KnowledgeCandidate, ...],
    ) -> dict[str, tuple[KnowledgeCandidate, ...]]:
        grouped: defaultdict[
            str,
            list[KnowledgeCandidate],
        ] = defaultdict(list)

        for candidate in candidates:
            grouped[candidate.category].append(candidate)

        return {category: tuple(values) for category, values in grouped.items()}
