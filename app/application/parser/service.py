"""Application service for repository parsing."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.parser.entities import ParsedDocument
from app.domain.parser.interfaces import Parser
from app.domain.scanner.entities import ScanDocument

from .models import ParseResponse


@dataclass(frozen=True, slots=True)
class ParserService:
    """Coordinate repository parsing."""

    parser: Parser

    def parse(
        self,
        documents: tuple[ScanDocument, ...],
    ) -> ParseResponse:
        """Parse scanned repository documents."""

        parsed: list[ParsedDocument] = [
            self.parser.parse(document) for document in documents
        ]

        return ParseResponse(
            documents=tuple(parsed),
        )
