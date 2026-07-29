from pathlib import PurePosixPath

from app.domain.content.entities import ContentMatch
from app.domain.parser.entities import ParsedDocument
from app.infrastructure.normalizer.local_normalizer import (
    LocalKnowledgeNormalizer,
)


def test_remove_duplicates() -> None:
    document = ParsedDocument(
        path=PurePosixPath("README.md"),
        language="markdown",
        title="Doc",
        plain_text="",
        sections=(),
        metadata={},
    )

    matches = [
        ContentMatch(
            category="technology",
            value="Python",
            source=document,
        ),
        ContentMatch(
            category="technology",
            value="python",
            source=document,
        ),
        ContentMatch(
            category="technology",
            value="Python3",
            source=document,
        ),
    ]

    normalizer = LocalKnowledgeNormalizer()

    result = normalizer.normalize(matches)

    assert len(result) == 1
    assert result[0].value == "python"


def test_postgresql_alias() -> None:
    document = ParsedDocument(
        path=PurePosixPath("README.md"),
        language="markdown",
        title="Doc",
        plain_text="",
        sections=(),
        metadata={},
    )

    matches = [
        ContentMatch(
            category="technology",
            value="Postgres",
            source=document,
        ),
    ]

    result = LocalKnowledgeNormalizer().normalize(matches)

    assert result[0].value == "postgresql"
