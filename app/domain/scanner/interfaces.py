"""Scanner domain interfaces."""

from __future__ import annotations

from abc import ABC, abstractmethod

from app.domain.repository.entities import RepositorySnapshot
from app.domain.scanner.entities import ScanResult


class Scanner(ABC):
    """Scanner contract."""

    @abstractmethod
    def scan(self, snapshot: RepositorySnapshot) -> ScanResult:
        """Read supported repository documents."""
