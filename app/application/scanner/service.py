"""Repository scanner application service."""

from __future__ import annotations

from dataclasses import dataclass

from app.domain.repository.entities import RepositorySnapshot
from app.domain.scanner.entities import ScanResult
from app.domain.scanner.interfaces import Scanner


@dataclass(frozen=True, slots=True)
class ScannerService:
    """Coordinate repository scanning."""

    scanner: Scanner

    def scan(self, snapshot: RepositorySnapshot) -> ScanResult:
        """Execute repository scanning."""

        return self.scanner.scan(snapshot)
