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

    assert relationships == (
        relationships[0],
        relationships[1],
    )

    assert len(relationships) == 2
    assert all(relationship.relation == "related_to" for relationship in relationships)


def test_duplicate_candidates_do_not_create_duplicate_relationships() -> None:
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
            category="framework",
            value="Django",
            confidence=1.0,
            source=PurePosixPath("pyproject.toml"),
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

    pairs = {
        (
            relationship.source,
            relationship.target,
            relationship.relation,
        )
        for relationship in relationships
    }

    assert pairs == {
        ("Django", "PostgreSQL", "related_to"),
        ("PostgreSQL", "Django", "related_to"),
    }


def test_relationships_are_created_only_between_different_categories() -> None:
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
            category="framework",
            value="FastAPI",
            confidence=1.0,
            source=PurePosixPath("README.md"),
        )
    )

    builder = KnowledgeRelationshipBuilder()

    relationships = builder.build(registry)

    assert relationships == ()
