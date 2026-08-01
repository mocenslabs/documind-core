from __future__ import annotations

from pathlib import Path

from pytest import CaptureFixture

from app.application.report.models import (
    RepositoryReport,
    RepositoryStatistics,
)
from app.domain.repository.entities import RepositorySnapshot
from app.domain.repository.value_objects import RepositoryReference
from app.presentation.console import print_report


def test_print_report(capsys: CaptureFixture[str]) -> None:
    repository = RepositorySnapshot(
        repository=RepositoryReference(locator="."),
        root_path=Path("."),
        files=(),
        directories=(),
    )

    report = RepositoryReport(
        repository=repository,
        statistics=RepositoryStatistics(
            total_files=10,
            python_files=5,
            markdown_files=2,
            test_files=3,
        ),
        knowledge=[],
        observations=(),
        recommendations=(),
        summary="Repository contains 10 files.",
    )

    print_report(report)

    captured = capsys.readouterr()

    assert "DOCUMIND ANALYSIS" in captured.out
    assert "Repository contains 10 files." in captured.out
