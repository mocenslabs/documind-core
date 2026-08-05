from pathlib import PurePosixPath

from app.application.knowledge.knowledge_deduplication import (
    KnowledgeDeduplicator,
)
from app.domain.knowledge.entities import Framework, Technology


def test_duplicate_knowledge_is_removed() -> None:
    deduplicator = KnowledgeDeduplicator()

    knowledge = (
        Technology(
            name="Node.js",
            source=PurePosixPath("package.json"),
        ),
        Technology(
            name="Node.js",
            source=PurePosixPath("frontend/package.json"),
        ),
        Technology(
            name="Node.js",
            source=PurePosixPath("packages/admin/package.json"),
        ),
    )

    result = deduplicator.deduplicate(knowledge)

    assert result == (
        Technology(
            name="Node.js",
            source=PurePosixPath("package.json"),
        ),
    )


def test_different_knowledge_types_are_not_merged() -> None:
    deduplicator = KnowledgeDeduplicator()

    knowledge = (
        Technology(
            name="Example",
            source=PurePosixPath("package.json"),
        ),
        Framework(
            name="Example",
            source=PurePosixPath("vite.config.ts"),
        ),
    )

    result = deduplicator.deduplicate(knowledge)

    assert result == knowledge


def test_different_knowledge_names_are_preserved() -> None:
    deduplicator = KnowledgeDeduplicator()

    knowledge = (
        Technology(
            name="Python",
            source=PurePosixPath("pyproject.toml"),
        ),
        Technology(
            name="Node.js",
            source=PurePosixPath("package.json"),
        ),
    )

    result = deduplicator.deduplicate(knowledge)

    assert result == knowledge
