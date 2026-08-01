from app.domain.report.entities import RepositoryReport


def test_report_entity_annotations() -> None:
    annotations = RepositoryReport.__annotations__

    assert "knowledge" in annotations
    assert "observations" in annotations
    assert "recommendations" in annotations
