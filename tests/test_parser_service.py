from pathlib import PurePosixPath

from app.application.parser.service import ParserService
from app.domain.parser.entities import ParsedDocument
from app.domain.parser.interfaces import Parser
from app.domain.scanner.entities import ScanDocument


class FakeParser(Parser):
    """Fake parser for tests."""

    def parse(
        self,
        document: ScanDocument,
    ) -> ParsedDocument:
        return ParsedDocument(
            path=document.path,
            language="markdown",
            title="README",
            plain_text=document.content,
            sections=(),
            metadata={},
        )


def test_parser_service() -> None:
    service = ParserService(
        parser=FakeParser(),
    )

    response = service.parse(
        (
            ScanDocument(
                path=PurePosixPath("README.md"),
                content="# Documind",
            ),
        )
    )

    assert len(response.documents) == 1

    document = response.documents[0]

    assert document.path == PurePosixPath("README.md")
    assert document.language == "markdown"
    assert document.title == "README"
    assert document.plain_text == "# Documind"
