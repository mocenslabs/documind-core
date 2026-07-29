from pathlib import PurePosixPath

from app.application.parser.models import ParseResponse
from app.domain.parser.entities import ParsedDocument


def test_parse_response() -> None:
    response = ParseResponse(
        documents=(
            ParsedDocument(
                path=PurePosixPath("README.md"),
                language="markdown",
                title="README",
                plain_text="# Documind",
                sections=(),
                metadata={},
            ),
        )
    )

    assert len(response.documents) == 1
