"""Construction tests for repository-loader contracts."""

from pathlib import Path

from app.application.repository_loader.models import RepositorySnapshotRequestModel
from app.domain.repository.entities import RepositorySnapshot
from app.domain.repository.interfaces import RepositoryLoader
from app.domain.repository.value_objects import (
    RepositoryReference,
    RepositorySnapshotRequest,
)


def test_repository_loader_contract_objects_construct() -> None:
    """Construct repository-loading contracts without repository access."""

    reference = RepositoryReference(
        locator="example/repository",
        revision="main",
    )

    request = RepositorySnapshotRequest(
        repository=reference,
    )

    request_model = RepositorySnapshotRequestModel(
        request=request,
    )

    snapshot = RepositorySnapshot(
        repository=reference,
        root_path=Path("example/repository"),
        files=(),
        directories=(),
    )

    assert request_model.request is request
    assert snapshot.repository is reference
    assert issubclass(RepositoryLoader, object)
