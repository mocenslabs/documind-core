from pathlib import PurePosixPath

from app.domain.parser.entities import ParsedDocument
from app.infrastructure.knowledge.local_extractor import (
    LocalKnowledgeExtractor,
)


def test_extract_multiple_candidates() -> None:
    extractor = LocalKnowledgeExtractor()

    parsed = ParsedDocument(
        path=PurePosixPath("README.md"),
        language="markdown",
        title="README",
        plain_text="""
        Django
        PostgreSQL
        Redis
        Docker
        GitHub Actions
        Ruff
        Black
        Pytest
        Celery
        Node.js
        Vite
        """,
        sections=(),
        metadata={},
    )

    result = extractor.extract((parsed,))

    values = {candidate.value for candidate in result}

    assert "Django" in values
    assert "PostgreSQL" in values
    assert "Redis" in values
    assert "Docker" in values
    assert "GitHub Actions" in values
    assert "Ruff" in values
    assert "Black" in values
    assert "Pytest" in values
    assert "Celery" in values
    assert "Node.js" in values
    assert "Vite" in values


def test_extract_does_not_match_substrings() -> None:
    extractor = LocalKnowledgeExtractor()

    parsed = ParsedDocument(
        path=PurePosixPath("README.md"),
        language="markdown",
        title="README",
        plain_text="""
        preview
        reactive
        blacklisted
        postgres_backup
        """,
        sections=(),
        metadata={},
    )

    result = extractor.extract((parsed,))

    values = {candidate.value for candidate in result}

    assert "Vue" not in values
    assert "React" not in values
    assert "Black" not in values
    assert "PostgreSQL" not in values


def test_high_confidence_source_for_package_json() -> None:
    extractor = LocalKnowledgeExtractor()

    parsed = ParsedDocument(
        path=PurePosixPath("package.json"),
        language="json",
        title="package.json",
        plain_text="""
        {
            "dependencies": {
                "vite": "^8.0.0"
            }
        }
        """,
        sections=(),
        metadata={},
    )

    result = extractor.extract((parsed,))

    vite = next(candidate for candidate in result if candidate.value == "Vite")

    assert vite.confidence == 1.0


def test_readme_source_has_high_but_not_maximum_confidence() -> None:
    extractor = LocalKnowledgeExtractor()

    parsed = ParsedDocument(
        path=PurePosixPath("README.md"),
        language="markdown",
        title="README",
        plain_text="This project uses Vite.",
        sections=(),
        metadata={},
    )

    result = extractor.extract((parsed,))

    vite = next(candidate for candidate in result if candidate.value == "Vite")

    assert vite.confidence == 0.9
