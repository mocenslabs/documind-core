from __future__ import annotations

from pathlib import Path

from app.application.analyze.models import AnalysisResult
from app.application.generation.context_builder import (
    ReadmeGenerationContextBuilder,
)
from app.application.generation.repository_service import (
    RepositoryReadmeGenerationService,
)
from app.application.generation.service import ReadmeGenerationService
from app.domain.generation.entities import GeneratedReadme
from app.domain.repository.entities import RepositorySnapshot
from app.domain.repository.value_objects import RepositoryReference
from app.infrastructure.generation.fake_provider import (
    FakeReadmeGenerationProvider,
)


def _analysis() -> AnalysisResult:
    repository = RepositorySnapshot(
        repository=RepositoryReference(locator="DocuMind"),
        root_path=Path("."),
        files=(),
        directories=(),
    )

    return AnalysisResult(
        repository=repository,
        scanned_documents=(),
        parsed_documents=(),
        facts=(),
        knowledge=(),
    )


def test_generate_builds_readme_from_analysis() -> None:
    service = RepositoryReadmeGenerationService(
        context_builder=ReadmeGenerationContextBuilder(),
        generation_service=ReadmeGenerationService(
            provider=FakeReadmeGenerationProvider(),
        ),
    )

    result = service.generate(_analysis())

    assert isinstance(result, GeneratedReadme)
    assert result.content.startswith("# DocuMind\n")
