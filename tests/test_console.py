from __future__ import annotations

from pathlib import Path, PurePosixPath

from pytest import CaptureFixture

from app.application.report.models import (
    RepositoryReport,
    RepositoryStatistics,
)
from app.domain.inference.category import ObservationCategory
from app.domain.inference.confidence import Confidence
from app.domain.inference.entities import Observation
from app.domain.inference.priority import Priority
from app.domain.inference.severity import Severity
from app.domain.knowledge.entities import Technology
from app.domain.recommendation.entities import Recommendation
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

    observation = Observation(
        code="framework.python",
        title="Python detected",
        description="Repository uses Python.",
        severity=Severity.INFO,
        priority=Priority.MEDIUM,
        category=ObservationCategory.ARCHITECTURE,
        confidence=Confidence.CERTAIN,
        actions=(),
    )

    recommendation = Recommendation(
        id="framework.python",
        title="Review Python runtime",
        description="Verify the supported Python version.",
        observation=observation,
    )

    report = RepositoryReport(
        repository=repository,
        statistics=RepositoryStatistics(
            total_files=10,
            python_files=5,
            markdown_files=2,
            test_files=3,
        ),
        knowledge=[
            Technology(
                name="Python",
                source=PurePosixPath("pyproject.toml"),
            )
        ],
        observations=(observation,),
        recommendations=(recommendation,),
        summary="Repository contains 10 files.",
    )

    print_report(report)

    captured = capsys.readouterr()

    assert "DOCUMIND ANALYSIS" in captured.out
    assert "Repository contains 10 files." in captured.out
    assert "Python" in captured.out
    assert "Observations" in captured.out
    assert "Python detected" in captured.out
    assert "Category  : architecture" in captured.out
    assert "Severity  : info" in captured.out
    assert "Priority  : medium" in captured.out
    assert "Confidence: certain" in captured.out
    assert "Recommendations" in captured.out
    assert "Review Python runtime" in captured.out
