from app.domain.inference.category import (
    ObservationCategory,
)


def test_categories() -> None:
    assert ObservationCategory.ARCHITECTURE.value == "architecture"

    assert ObservationCategory.SECURITY.value == "security"

    assert ObservationCategory.DEVOPS.value == "devops"
