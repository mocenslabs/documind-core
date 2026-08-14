from __future__ import annotations

from pathlib import Path

from app.application.analyze.service import AnalyzeRepositoryService
from app.application.bootstrap import create_analyzer
from app.domain.repository.value_objects import (
    RepositoryReference,
    RepositorySnapshotRequest,
)


def test_create_analyzer_returns_analyze_repository_service() -> None:
    analyzer = create_analyzer()

    assert isinstance(analyzer, AnalyzeRepositoryService)


def test_create_analyzer_builds_a_usable_pipeline(tmp_path: Path) -> None:
    """The composition root must wire every collaborator correctly.

    Since AnalyzeRepositoryService keeps its collaborators private, the
    only reliable way to prove the wiring is correct is behavioral: run
    a real analysis end-to-end against a throwaway repository and check
    it completes without error and returns a sane result.
    """

    (tmp_path / "pyproject.toml").write_text(
        '[project]\nname = "sample"\n',
        encoding="utf-8",
    )
    (tmp_path / "README.md").write_text(
        "# Sample\n",
        encoding="utf-8",
    )

    analyzer = create_analyzer()

    request = RepositorySnapshotRequest(
        repository=RepositoryReference(
            locator=str(tmp_path),
        ),
    )

    result = analyzer.analyze(request)

    assert result.repository.root_path == tmp_path.resolve()
    assert result.knowledge is not None
    assert result.observations is not None
    assert result.recommendations is not None


def test_create_analyzer_returns_a_new_instance_each_call() -> None:
    """Each call must build a fresh, independent service instance.

    Guards against someone turning this into a cached singleton later
    (e.g. for reuse across API requests) without noticing the pipeline
    services are not designed to be shared/thread-safe.
    """

    first = create_analyzer()
    second = create_analyzer()

    assert first is not second
