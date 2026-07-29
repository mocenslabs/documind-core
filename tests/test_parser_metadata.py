from pathlib import PurePosixPath

from app.domain.parser.entities import ParsedDocument


def test_metadata_is_available() -> None:
    document = ParsedDocument(
        path=PurePosixPath("README.md"),
        language="markdown",
        title="README",
        plain_text="content",
        sections=(),
        metadata={
            "filename": "README.md",
        },
    )

    assert document.metadata["filename"] == "README.md"
