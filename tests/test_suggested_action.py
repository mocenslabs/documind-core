from app.domain.inference.actions import SuggestedAction


def test_action() -> None:
    action = SuggestedAction(
        title="Review",
        description="Inspect configuration.",
    )

    assert action.title == "Review"
