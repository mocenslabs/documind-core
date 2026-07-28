"""Parser domain contracts."""

from __future__ import annotations

from abc import ABC, abstractmethod

from app.domain.scanner.entities import ScanDocument

from .entities import ParsedDocument


class Parser(ABC):
    """Normalize scanned documents."""

    @abstractmethod
    def parse(
        self,
        document: ScanDocument,
    ) -> ParsedDocument:
        """Parse a scanned document."""
