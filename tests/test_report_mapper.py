from pathlib import Path

from app.application.analyze.models import AnalysisResult
from app.application.report.mapper import RepositoryReportMapper
from app.application.report.models import RepositoryStatistics
from app.domain.inference.category import ObservationCategory
from app.domain.inference.confidence import Confidence
from app.domain.inference.entities import Observation
from app.domain.inference.priority import Priority
from app.domain.inference.severity import Severity
from app.domain.recommendation.entities import Recommendation
from app.domain.repository.entities import RepositorySnapshot
from app.domain.repository.value_objects import RepositoryReference


def test_report_mapper() -> None:
    repository = RepositorySnapshot(
        repository=RepositoryReference(
            locator=".",
        ),
        root_path=Path("."),
        files=(),
        directories=(),
    )

    observation = Observation(
        code="framework.python",
        title="Python detected",
        description="Repository uses Python.",
        category=ObservationCategory.ARCHITECTURE,
        severity=Severity.INFO,
        priority=Priority.MEDIUM,
        confidence=Confidence.CERTAIN,
    )

    recommendation = Recommendation(
        id="framework.python",
        title="Python detected",
        description="Repository uses Python.",
        observation=observation,
    )

    analysis = AnalysisResult(
        repository=repository,
        scanned_documents=(),
        parsed_documents=(),
        facts=[],
        knowledge=[],
        observations=(observation,),
        recommendations=(recommendation,),
    )

    statistics = RepositoryStatistics(
        total_files=0,
        python_files=0,
        markdown_files=0,
        test_files=0,
    )

    report = RepositoryReportMapper().map(
        analysis,
        statistics,
        "Repository contains 0 files (0 Python, 0 Markdown).",
    )

    assert report.repository == repository
    assert report.statistics == statistics
    assert report.knowledge == []
    assert report.observations == (observation,)
    assert report.recommendations == (recommendation,)
    assert report.summary == ("Repository contains 0 files (0 Python, 0 Markdown).")
