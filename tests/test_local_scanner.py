from pathlib import Path, PurePosixPath

from app.domain.repository.entities import RepositorySnapshot
from app.domain.repository.value_objects import RepositoryReference
from app.infrastructure.scanner.local_scanner import LocalScanner


def test_local_scanner_reads_supported_files(tmp_path: Path) -> None:
    readme = tmp_path / "README.md"
    readme.write_text("# Test", encoding="utf-8")

    snapshot = RepositorySnapshot(
        repository=RepositoryReference(locator=str(tmp_path)),
        root_path=tmp_path,
        files=(PurePosixPath("README.md"),),
        directories=(),
    )

    scanner = LocalScanner()

    result = scanner.scan(snapshot)

    assert len(result.documents) == 1
    assert result.documents[0].path == PurePosixPath("README.md")
    assert result.documents[0].content == "# Test"


def test_local_scanner_ignores_unknown_files(tmp_path: Path) -> None:
    file = tmp_path / "notes.txt"
    file.write_text("ignored", encoding="utf-8")

    snapshot = RepositorySnapshot(
        repository=RepositoryReference(locator=str(tmp_path)),
        root_path=tmp_path,
        files=(PurePosixPath("notes.txt"),),
        directories=(),
    )

    scanner = LocalScanner()

    result = scanner.scan(snapshot)

    assert result.documents == ()
