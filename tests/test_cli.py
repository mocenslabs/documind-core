from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from app.presentation.cli import app

runner = CliRunner()


def test_analyze_runs_against_a_valid_repository(tmp_path: Path) -> None:
    (tmp_path / "pyproject.toml").write_text(
        '[project]\nname = "sample"\n',
        encoding="utf-8",
    )

    result = runner.invoke(
        app,
        ["analyze", str(tmp_path)],
    )

    assert result.exit_code == 0
    assert "DOCUMIND ANALYSIS" in result.stdout


def test_analyze_defaults_to_current_directory_when_no_path_given() -> None:
    result = runner.invoke(
        app,
        ["analyze"],
    )

    assert result.exit_code == 0
    assert "DOCUMIND ANALYSIS" in result.stdout


def test_analyze_rejects_a_nonexistent_path(tmp_path: Path) -> None:
    missing_path = tmp_path / "does-not-exist"

    result = runner.invoke(
        app,
        ["analyze", str(missing_path)],
    )

    assert result.exit_code != 0


def test_analyze_rejects_a_path_that_is_a_file(tmp_path: Path) -> None:
    file_path = tmp_path / "not-a-directory.txt"
    file_path.write_text("content", encoding="utf-8")

    result = runner.invoke(
        app,
        ["analyze", str(file_path)],
    )

    assert result.exit_code != 0


def test_generate_readme_runs_against_a_valid_repository(
    tmp_path: Path,
) -> None:
    (tmp_path / "pyproject.toml").write_text(
        '[project]\nname = "sample"\n',
        encoding="utf-8",
    )

    result = runner.invoke(
        app,
        ["generate-readme", str(tmp_path)],
    )

    assert result.exit_code == 0
    assert result.stdout.startswith("# ")
    assert "## Technologies" in result.stdout
    assert "## Frameworks" in result.stdout
    assert "## Containers" in result.stdout
    assert "## CI Platforms" in result.stdout
    assert "## Observations" in result.stdout
    assert "## Recommendations" in result.stdout


def test_generate_readme_defaults_to_current_directory() -> None:
    result = runner.invoke(
        app,
        ["generate-readme"],
    )

    assert result.exit_code == 0
    assert result.stdout.startswith("# ")


def test_generate_readme_rejects_a_nonexistent_path(
    tmp_path: Path,
) -> None:
    missing_path = tmp_path / "does-not-exist"

    result = runner.invoke(
        app,
        ["generate-readme", str(missing_path)],
    )

    assert result.exit_code != 0


def test_generate_readme_rejects_a_path_that_is_a_file(
    tmp_path: Path,
) -> None:
    file_path = tmp_path / "not-a-directory.txt"
    file_path.write_text(
        "content",
        encoding="utf-8",
    )

    result = runner.invoke(
        app,
        ["generate-readme", str(file_path)],
    )

    assert result.exit_code != 0
