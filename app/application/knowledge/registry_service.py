"""Knowledge registry service."""

from __future__ import annotations

from app.domain.knowledge.entities import (
    KnowledgeCandidate,
    KnowledgeRegistry,
)


class KnowledgeRegistryService:
    """Populate repository knowledge registry."""

    def build(
        self,
        candidates: tuple[
            KnowledgeCandidate,
            ...,
        ],
    ) -> KnowledgeRegistry:
        """Build a knowledge registry."""

        registry = KnowledgeRegistry()

        for candidate in candidates:
            registry.add(candidate)

        return registry
