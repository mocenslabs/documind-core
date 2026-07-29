from pathlib import PurePosixPath

from app.application.knowledge.service import KnowledgeExtractionService
from app.domain.knowledge.entities import KnowledgeCandidate
from app.domain.knowledge.interfaces import KnowledgeExtractor
from app.domain.parser.entities import ParsedDocument


class FakeExtractor(KnowledgeExtractor):
    def extract(
        self,
        documents: tuple[ParsedDocument, ...],
    ) -> list[KnowledgeCandidate]:
        return [
            KnowledgeCandidate(
                category="framework",
                value="Django",
                confidence=1.0,
                source=PurePosixPath("README.md"),
            )
        ]


def test_extract_knowledge() -> None:
    service = KnowledgeExtractionService(
        extractor=FakeExtractor(),
    )

    response = service.extract(
        (
            ParsedDocument(
                path=PurePosixPath("README.md"),
                language="markdown",
                title="README",
                plain_text="Uses Django",
                sections=(),
                metadata={},
            ),
        )
    )

    assert len(response.candidates) == 1
    assert response.candidates[0].value == "Django"


def test_duplicate_candidates_are_removed() -> None:
    class DuplicateExtractor(KnowledgeExtractor):
        def extract(
            self,
            documents: tuple[ParsedDocument, ...],
        ) -> list[KnowledgeCandidate]:
            return [
                KnowledgeCandidate(
                    category="framework",
                    value="Django",
                    confidence=1.0,
                    source=PurePosixPath("README.md"),
                ),
                KnowledgeCandidate(
                    category="framework",
                    value="Django",
                    confidence=1.0,
                    source=PurePosixPath("pyproject.toml"),
                ),
            ]

    service = KnowledgeExtractionService(
        extractor=DuplicateExtractor(),
    )

    response = service.extract(
        (
            ParsedDocument(
                path=PurePosixPath("README.md"),
                language="markdown",
                title="README",
                plain_text="Django",
                sections=(),
                metadata={},
            ),
        )
    )

    assert len(response.candidates) == 1
