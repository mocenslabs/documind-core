"""Repository report service."""

from __future__ import annotations

from pathlib import PurePosixPath

from app.application.analyze.models import AnalysisResult
from app.application.report.models import (
    RepositoryReport,
    RepositoryStatistics,
)


class RepositoryReportService:
    """Build a human-readable repository report."""

    def build(
        self,
        analysis: AnalysisResult,
    ) -> RepositoryReport:
        files: tuple[PurePosixPath, ...] = analysis.repository.files

        python_files = [path for path in files if path.suffix == ".py"]

        markdown_files = [path for path in files if path.suffix == ".md"]

        test_files = [
            path
            for path in files
            if path.name.startswith("test_") or path.parent.name == "tests"
        ]

        statistics = RepositoryStatistics(
            total_files=len(files),
            python_files=len(python_files),
            markdown_files=len(markdown_files),
            test_files=len(test_files),
        )

        summary = (
            f"Repository contains "
            f"{statistics.total_files} files "
            f"({statistics.python_files} Python, "
            f"{statistics.markdown_files} Markdown)."
        )

        return RepositoryReport(
            repository=analysis.repository,
            statistics=statistics,
            knowledge=analysis.knowledge,
            summary=summary,
        )
