"""Report domain contracts."""

from __future__ import annotations

from abc import ABC, abstractmethod

from .entities import RepositoryReport


class ReportRenderer(ABC):
    """Render repository reports."""

    @abstractmethod
    def render(
        self,
        report: RepositoryReport,
    ) -> str:
        """Render a report."""
