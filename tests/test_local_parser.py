from pathlib import PurePosixPath

from app.domain.scanner.entities import ScanDocument
from app.infrastructure.parser.local_parser import LocalParser


def test_parse_markdown_document() -> None:
    parser = LocalParser()

    document = ScanDocument(
        path=PurePosixPath("README.md"),
        content=(
            "# DocuMind\n"
            "\n"
            "Repository analyzer.\n"
            "\n"
            "## Installation\n"
            "\n"
            "pip install\n"
        ),
    )

    result = parser.parse(document)

    assert result.language == "markdown"
    assert result.title == "DocuMind"
    assert len(result.sections) == 2


def test_parse_non_markdown_document() -> None:
    parser = LocalParser()

    document = ScanDocument(
        path=PurePosixPath("pyproject.toml"),
        content="[project]",
    )

    result = parser.parse(document)

    assert result.language == "toml"
    assert result.title == "pyproject.toml"
    assert result.sections == ()
