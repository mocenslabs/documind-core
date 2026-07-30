from app.domain.inference.priority import Priority


def test_priority_values() -> None:
    assert Priority.LOW.value == 1
    assert Priority.MEDIUM.value == 2
    assert Priority.HIGH.value == 3
    assert Priority.CRITICAL.value == 4
