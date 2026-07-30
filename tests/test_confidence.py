from app.domain.inference.confidence import Confidence


def test_confidence_values() -> None:
    assert Confidence.LOW.value == 25
    assert Confidence.MEDIUM.value == 50
    assert Confidence.HIGH.value == 75
    assert Confidence.CERTAIN.value == 100
