"""Parser application service."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.parser.interfaces import Parser
from app.domain.scanner.entities import ScanResult

from .models import ParseResponse


@dataclass(frozen=True, slots=True)
class ParserService:
    """Coordinate repository document parsing."""

    parser: Parser

    def parse(
        self,
        scan_result: ScanResult,
    ) -> ParseResponse:
        """Parse every scanned document."""

        documents = tuple(
            self.parser.parse(document) for document in scan_result.documents
        )

        return ParseResponse(
            documents=documents,
        )
