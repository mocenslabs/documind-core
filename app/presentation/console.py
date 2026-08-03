"""Console output helpers."""

from __future__ import annotations

from app.application.report.models import RepositoryReport


def print_report(report: RepositoryReport) -> None:
    """Print a human-readable repository report."""

    print()
    print("=" * 60)
    print("DOCUMIND ANALYSIS")
    print("=" * 60)

    print(f"Repository : {report.repository.repository.locator}")
    print()

    print("Statistics")
    print("-" * 60)
    print(f"Files      : {report.statistics.total_files}")
    print(f"Python     : {report.statistics.python_files}")
    print(f"Markdown   : {report.statistics.markdown_files}")
    print(f"Tests      : {report.statistics.test_files}")

    print()

    print("Knowledge")
    print("-" * 60)

    if report.knowledge:
        for item in report.knowledge:
            print(f"- {item.name}")
    else:
        print("No knowledge detected.")

    print()

    print("Observations")
    print("-" * 60)

    if report.observations:
        for observation in report.observations:
            print(f"- {observation.title}")
            print(f"  {observation.description}")
    else:
        print("No observations generated.")

    print()

    print("Recommendations")
    print("-" * 60)

    if report.recommendations:
        for recommendation in report.recommendations:
            print(f"- {recommendation.title}")
            print(f"  {recommendation.description}")
    else:
        print("No recommendations generated.")

    print()

    print("Summary")
    print("-" * 60)
    print(report.summary)
    print()
