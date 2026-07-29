from pathlib import PurePosixPath

from app.application.knowledge.relationship_builder import (
    KnowledgeRelationshipBuilder,
)
from app.domain.knowledge.entities import (
    KnowledgeCandidate,
    KnowledgeRegistry,
)


def test_build_relationships() -> None:
    registry = KnowledgeRegistry()

    registry.add(
        KnowledgeCandidate(
            category="framework",
            value="Django",
            confidence=1.0,
            source=PurePosixPath("README.md"),
        )
    )

    registry.add(
        KnowledgeCandidate(
            category="database",
            value="PostgreSQL",
            confidence=1.0,
            source=PurePosixPath("README.md"),
        )
    )

    builder = KnowledgeRelationshipBuilder()

    relationships = builder.build(registry)

    assert len(relationships) == 2

    assert relationships[0].relation == "related_to"
