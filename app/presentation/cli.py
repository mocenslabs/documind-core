"""Command-line interface."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from app.application.bootstrap import (
    create_analyzer,
    create_readme_generator,
)
from app.application.report.service import RepositoryReportService
from app.domain.repository.value_objects import (
    RepositoryReference,
    RepositorySnapshotRequest,
)
from app.presentation.console import print_report

app = typer.Typer(
    name="documind",
    help="AI-powered repository analysis.",
    no_args_is_help=True,
)

PathArgument = Annotated[
    Path,
    typer.Argument(
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        help="Repository path.",
    ),
]


@app.command()
def analyze(path: PathArgument = Path(".")) -> None:
    """Analyze a repository."""

    analyzer = create_analyzer()

    request = RepositorySnapshotRequest(
        repository=RepositoryReference(
            locator=str(path),
        ),
    )

    analysis = analyzer.analyze(request)

    report = RepositoryReportService().build(analysis)

    print_report(report)


@app.command("generate-readme")
def generate_readme(path: PathArgument = Path(".")) -> None:
    """Generate a README for a repository."""

    analyzer = create_analyzer()
    generator = create_readme_generator()

    request = RepositorySnapshotRequest(
        repository=RepositoryReference(
            locator=str(path),
        ),
    )

    analysis = analyzer.analyze(request)
    readme = generator.generate(analysis)

    print(readme.content, end="")


if __name__ == "__main__":
    app()
