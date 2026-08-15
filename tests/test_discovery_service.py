"""Tests for deterministic snapshot discovery."""

from pathlib import Path, PurePosixPath

from app.application.discovery.service import DiscoveryService
from app.domain.discovery.facts import FoundDirectory, FoundFile, RawFact
from app.domain.repository.entities import RepositorySnapshot
from app.domain.repository.value_objects import RepositoryReference


def _snapshot(
    *,
    files: tuple[PurePosixPath, ...] = (),
    directories: tuple[PurePosixPath, ...] = (),
) -> RepositorySnapshot:
    """Create a path-only snapshot for discovery tests."""
    return RepositorySnapshot(
        repository=RepositoryReference(locator="example/repository"),
        root_path=Path("example/repository"),
        files=files,
        directories=directories,
    )


def test_discovery_service_returns_no_facts_for_empty_snapshot() -> None:
    """Return an empty fact list when the snapshot inventory is empty."""
    assert DiscoveryService().discover(_snapshot()) == []


def test_discovery_service_returns_found_file_facts() -> None:
    """Convert snapshot files into found-file facts."""
    facts = DiscoveryService().discover(
        _snapshot(
            files=(
                PurePosixPath("src/main.py"),
                PurePosixPath("README.md"),
            )
        )
    )

    assert facts == [
        FoundFile(PurePosixPath("README.md")),
        FoundFile(PurePosixPath("src/main.py")),
    ]


def test_discovery_service_returns_found_directory_facts() -> None:
    """Convert snapshot directories into found-directory facts."""
    facts = DiscoveryService().discover(
        _snapshot(
            directories=(
                PurePosixPath("src"),
                PurePosixPath("docs"),
            )
        )
    )

    assert facts == [
        FoundDirectory(PurePosixPath("docs")),
        FoundDirectory(PurePosixPath("src")),
    ]


def test_discovery_service_orders_mixed_facts_deterministically() -> None:
    """Order mixed facts by path and fact type."""
    facts: list[RawFact] = DiscoveryService().discover(
        _snapshot(
            files=(
                PurePosixPath("z.py"),
                PurePosixPath("a.py"),
            ),
            directories=(PurePosixPath("docs"),),
        )
    )

    assert facts == [
        FoundFile(PurePosixPath("a.py")),
        FoundDirectory(PurePosixPath("docs")),
        FoundFile(PurePosixPath("z.py")),
    ]


def test_discovery_service_excludes_generated_directories() -> None:
    """Ignore common generated and dependency directories."""
    facts = DiscoveryService().discover(
        _snapshot(
            files=(
                PurePosixPath("src/main.py"),
                PurePosixPath("node_modules/package/index.js"),
                PurePosixPath(".venv/lib/python3.12/site.py"),
                PurePosixPath("__pycache__/module.pyc"),
                PurePosixPath("dist/bundle.js"),
                PurePosixPath("build/output.js"),
                PurePosixPath(".git/config"),
            ),
            directories=(
                PurePosixPath("src"),
                PurePosixPath("node_modules"),
                PurePosixPath(".venv"),
                PurePosixPath("__pycache__"),
                PurePosixPath("dist"),
                PurePosixPath("build"),
                PurePosixPath(".git"),
            ),
        )
    )

    assert facts == [
        FoundDirectory(PurePosixPath("src")),
        FoundFile(PurePosixPath("src/main.py")),
    ]


def test_discovery_service_excludes_nested_generated_directories() -> None:
    """Ignore excluded directories regardless of their nesting level."""
    facts = DiscoveryService().discover(
        _snapshot(
            files=(
                PurePosixPath("src/node_modules/package/index.js"),
                PurePosixPath("services/api/__pycache__/module.pyc"),
                PurePosixPath("apps/web/dist/assets/index.js"),
                PurePosixPath("src/application.py"),
            ),
            directories=(
                PurePosixPath("src/node_modules"),
                PurePosixPath("services/api/__pycache__"),
                PurePosixPath("apps/web/dist"),
                PurePosixPath("src"),
            ),
        )
    )

    assert facts == [
        FoundDirectory(PurePosixPath("src")),
        FoundFile(PurePosixPath("src/application.py")),
    ]


def test_discovery_service_preserves_similarly_named_directories() -> None:
    """Only exact excluded directory names should be filtered."""
    facts = DiscoveryService().discover(
        _snapshot(
            files=(
                PurePosixPath("src/node_modules_backup/index.js"),
                PurePosixPath("src/build_tools/main.py"),
                PurePosixPath("src/main.py"),
            ),
            directories=(
                PurePosixPath("src"),
                PurePosixPath("src/node_modules_backup"),
                PurePosixPath("src/build_tools"),
            ),
        )
    )

    assert facts == [
        FoundDirectory(PurePosixPath("src")),
        FoundDirectory(PurePosixPath("src/build_tools")),
        FoundFile(PurePosixPath("src/build_tools/main.py")),
        FoundFile(PurePosixPath("src/main.py")),
        FoundDirectory(PurePosixPath("src/node_modules_backup")),
        FoundFile(PurePosixPath("src/node_modules_backup/index.js")),
    ]
