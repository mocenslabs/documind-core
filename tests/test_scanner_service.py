from pathlib import PurePosixPath

from app.application.scanner.service import ScannerService
from app.domain.repository.entities import RepositorySnapshot
from app.domain.repository.value_objects import RepositoryReference
from app.domain.scanner.entities import ScanDocument, ScanResult
from app.domain.scanner.interfaces import Scanner


class FakeScanner(Scanner):
    def scan(self, snapshot: RepositorySnapshot) -> ScanResult:
        return ScanResult(
            documents=(
                ScanDocument(
                    path=PurePosixPath("README.md"),
                    content="# Documind",
                ),
            ),
        )


def test_scanner_service() -> None:
    snapshot = RepositorySnapshot(
        repository=RepositoryReference(locator="."),
        root_path=PurePosixPath("."),  # type: ignore[arg-type]
        files=(),
        directories=(),
    )

    service = ScannerService(
        scanner=FakeScanner(),
    )

    response = service.scan(snapshot)

    assert len(response.documents) == 1

    document = response.documents[0]

    assert document.path == PurePosixPath("README.md")

    assert document.content == "# Documind"
