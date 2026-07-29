from pathlib import Path, PurePosixPath

from app.application.analyze.models import AnalysisResult
from app.application.report.service import RepositoryReportService
from app.domain.repository.entities import RepositorySnapshot
from app.domain.repository.value_objects import RepositoryReference
from app.domain.scanner.entities import ScanDocument


def test_build_report() -> None:
    repository = RepositorySnapshot(
        repository=RepositoryReference(locator="."),
        root_path=Path("."),
        files=(
            PurePosixPath("main.py"),
            PurePosixPath("README.md"),
            PurePosixPath("tests/test_app.py"),
        ),
        directories=(),
    )

    analysis = AnalysisResult(
        repository=repository,
        scanned_documents=(
            ScanDocument(
                path=PurePosixPath("README.md"),
                content="# Documind",
            ),
        ),
        parsed_documents=(),
        facts=[],
        knowledge=[],
    )

    report = RepositoryReportService().build(analysis)

    assert report.statistics.total_files == 3
    assert report.statistics.python_files == 2
    assert report.statistics.markdown_files == 1
    assert report.statistics.test_files == 1
