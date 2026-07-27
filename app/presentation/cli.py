"""Command-line interface."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from app.application.analyze.service import AnalyzeRepositoryService
from app.application.discovery.service import DiscoveryService
from app.application.knowledge.service import KnowledgeService
from app.application.report.service import RepositoryReportService
from app.application.rules.builtin_rules import builtin_rules
from app.application.rules.service import RuleEngineService
from app.application.scanner.service import ScannerService
from app.domain.repository.value_objects import (
    RepositoryReference,
    RepositorySnapshotRequest,
)
from app.infrastructure.repository_loader.local_loader import LocalRepositoryLoader
from app.infrastructure.scanner.local_scanner import LocalScanner
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

    loader = LocalRepositoryLoader()

    scanner_service = ScannerService(
        scanner=LocalScanner(),
    )

    discovery_service = DiscoveryService()

    rule_engine = RuleEngineService(
        rules=builtin_rules(),
    )

    knowledge_service = KnowledgeService(
        rule_engine=rule_engine,
    )

    analyzer = AnalyzeRepositoryService(
        repository_loader=loader,
        scanner_service=scanner_service,
        discovery_service=discovery_service,
        knowledge_service=knowledge_service,
    )

    request = RepositorySnapshotRequest(
        repository=RepositoryReference(
            locator=str(path),
        ),
    )

    analysis = analyzer.analyze(request)

    report = RepositoryReportService().build(analysis)

    print_report(report)


if __name__ == "__main__":
    app()
