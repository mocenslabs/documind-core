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

    result = runner.invoke(app, [str(tmp_path)])

    assert result.exit_code == 0
    assert "DOCUMIND ANALYSIS" in result.stdout


def test_analyze_defaults_to_current_directory_when_no_path_given() -> None:
    result = runner.invoke(app, [])

    assert result.exit_code == 0
    assert "DOCUMIND ANALYSIS" in result.stdout


def test_analyze_rejects_a_nonexistent_path(tmp_path: Path) -> None:
    missing_path = tmp_path / "does-not-exist"

    result = runner.invoke(app, [str(missing_path)])

    assert result.exit_code != 0


def test_analyze_rejects_a_path_that_is_a_file(tmp_path: Path) -> None:
    file_path = tmp_path / "not-a-directory.txt"
    file_path.write_text("content", encoding="utf-8")

    result = runner.invoke(app, [str(file_path)])

    assert result.exit_code != 0
