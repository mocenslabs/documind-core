"""Repository report service."""

from __future__ import annotations

from pathlib import PurePosixPath

from app.application.analyze.models import AnalysisResult

from .mapper import RepositoryReportMapper
from .models import RepositoryReport, RepositoryStatistics


class RepositoryReportService:
    """Build a human-readable repository report."""

    def __init__(
        self,
        mapper: RepositoryReportMapper | None = None,
    ) -> None:
        self._mapper = mapper or RepositoryReportMapper()

    def build(
        self,
        analysis: AnalysisResult,
    ) -> RepositoryReport:
        """Build a repository report."""

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

        return self._mapper.map(
            analysis,
            statistics,
            summary,
        )
