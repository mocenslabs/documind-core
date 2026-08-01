"""Map analysis results into repository reports."""

from __future__ import annotations

from app.application.analyze.models import AnalysisResult

from .models import RepositoryReport, RepositoryStatistics


class RepositoryReportMapper:
    """Map an analysis result to a repository report."""

    def map(
        self,
        analysis: AnalysisResult,
        statistics: RepositoryStatistics,
        summary: str,
    ) -> RepositoryReport:
        """Create a report from an analysis result."""

        return RepositoryReport(
            repository=analysis.repository,
            statistics=statistics,
            knowledge=analysis.knowledge,
            observations=analysis.observations,
            recommendations=analysis.recommendations,
            summary=summary,
        )
