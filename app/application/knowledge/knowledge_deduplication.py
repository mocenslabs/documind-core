"""Knowledge deduplication."""

from __future__ import annotations

from app.domain.knowledge.entities import Knowledge


class KnowledgeDeduplicator:
    """Remove duplicated normalized knowledge."""

    def deduplicate(
        self,
        knowledge: tuple[Knowledge, ...],
    ) -> tuple[Knowledge, ...]:
        """Keep one knowledge item per type and normalized name."""

        unique: dict[tuple[type[Knowledge], str], Knowledge] = {}

        for item in knowledge:
            key = (
                type(item),
                item.name.casefold(),
            )

            if key not in unique:
                unique[key] = item

        return tuple(unique.values())
