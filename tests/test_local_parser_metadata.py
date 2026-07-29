from pathlib import PurePosixPath

from app.domain.scanner.entities import ScanDocument
from app.infrastructure.parser.local_parser import LocalParser


def test_parser_extracts_metadata() -> None:
    parser = LocalParser()

    parsed = parser.parse(
        ScanDocument(
            path=PurePosixPath("README.md"),
            content="# Documind\nHello",
        )
    )

    assert parsed.metadata["filename"] == "README.md"
    assert parsed.metadata["extension"] == ".md"
    assert parsed.metadata["lines"] == "2"
    assert parsed.metadata["first_line"] == "# Documind"
