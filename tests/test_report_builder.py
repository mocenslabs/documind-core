from app.domain.report.builder import RepositoryReportBuilder


def test_report_builder() -> None:
    builder = RepositoryReportBuilder()

    report = builder.build(
        knowledge=(),
        observations=(),
        recommendations=(),
    )

    assert report.knowledge == ()
    assert report.observations == ()
    assert report.recommendations == ()
