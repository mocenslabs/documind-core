"""Deterministic knowledge normalizer."""

from __future__ import annotations

from app.domain.content.entities import ContentMatch
from app.domain.normalizer.entities import NormalizedKnowledge
from app.domain.normalizer.interfaces import KnowledgeNormalizer


class LocalKnowledgeNormalizer(KnowledgeNormalizer):
    """Normalize duplicated knowledge."""

    _ALIASES = {
        "postgres": "postgresql",
        "postgresql": "postgresql",
        "py": "python",
        "python3": "python",
        "docker compose": "docker-compose",
        "docker-compose": "docker-compose",
    }

    def normalize(
        self,
        matches: list[ContentMatch],
    ) -> list[NormalizedKnowledge]:
        unique: dict[tuple[str, str], NormalizedKnowledge] = {}

        for match in matches:
            value = match.value.lower().strip()

            value = self._ALIASES.get(
                value,
                value,
            )

            key = (
                match.category,
                value,
            )

            if key not in unique:
                unique[key] = NormalizedKnowledge(
                    category=match.category,
                    value=value,
                )

        return sorted(
            unique.values(),
            key=lambda item: (
                item.category,
                item.value,
            ),
        )
