from pathlib import PurePosixPath

from app.domain.parser.entities import ParsedDocument
from app.infrastructure.content.local_content_discovery import (
    LocalContentDiscovery,
)


def test_detect_python_and_django() -> None:
    engine = LocalContentDiscovery()

    document = ParsedDocument(
        path=PurePosixPath("README.md"),
        language="markdown",
        title="Doc",
        plain_text="""
Python
Django
Redis
Docker
""",
        sections=(),
        metadata={},
    )

    matches = engine.discover((document,))

    values = {match.value for match in matches}

    assert "python" in values
    assert "django" in values
    assert "redis" in values
    assert "docker" in values


def test_empty_document() -> None:
    engine = LocalContentDiscovery()

    document = ParsedDocument(
        path=PurePosixPath("README.md"),
        language="markdown",
        title="Empty",
        plain_text="Nothing interesting here.",
        sections=(),
        metadata={},
    )

    matches = engine.discover((document,))

    assert matches == []
