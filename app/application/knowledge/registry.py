"""Knowledge registry."""

from __future__ import annotations

from dataclasses import dataclass, field

from app.domain.knowledge.entities import KnowledgeCandidate


@dataclass(slots=True)
class KnowledgeRegistry:
    """Structured repository knowledge."""

    categories: dict[
        str,
        list[KnowledgeCandidate],
    ] = field(default_factory=dict)

    def add(
        self,
        candidate: KnowledgeCandidate,
    ) -> None:
        """Register a knowledge candidate."""

        self.categories.setdefault(
            candidate.category,
            [],
        ).append(candidate)

    def get(
        self,
        category: str,
    ) -> tuple[KnowledgeCandidate, ...]:
        """Return candidates of one category."""

        return tuple(
            self.categories.get(
                category,
                [],
            )
        )

    def all(
        self,
    ) -> dict[
        str,
        tuple[KnowledgeCandidate, ...],
    ]:
        """Return all categories."""

        return {category: tuple(values) for category, values in self.categories.items()}
