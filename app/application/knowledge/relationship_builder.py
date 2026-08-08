"""Knowledge relationship builder."""

from __future__ import annotations

from app.domain.knowledge.entities import KnowledgeRegistry
from app.domain.knowledge.relationships import KnowledgeRelationship


class KnowledgeRelationshipBuilder:
    """Build simple relationships between detected technologies."""

    def build(
        self,
        registry: KnowledgeRegistry,
    ) -> tuple[KnowledgeRelationship, ...]:
        """Create relationships from a registry."""

        relationships: set[tuple[str, str, str]] = set()

        categories = registry.all()

        for values in categories.values():
            for candidate in values:
                for other_category, other_values in categories.items():
                    if other_category == candidate.category:
                        continue

                    for other in other_values:
                        relationships.add(
                            (
                                candidate.value,
                                other.value,
                                "related_to",
                            )
                        )

        return tuple(
            KnowledgeRelationship(
                source=source,
                target=target,
                relation=relation,
            )
            for source, target, relation in sorted(relationships)
        )
