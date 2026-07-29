from pathlib import PurePosixPath

from app.domain.knowledge.entities import (
    KnowledgeCandidate,
    KnowledgeRegistry,
)


def test_registry_add() -> None:
    registry = KnowledgeRegistry()

    registry.add(
        KnowledgeCandidate(
            category="framework",
            value="Django",
            confidence=1.0,
            source=PurePosixPath("README.md"),
        )
    )

    assert len(registry.get("framework")) == 1
