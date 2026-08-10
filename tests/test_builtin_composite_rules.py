from app.application.inference.builtin_composite_rules import (
    builtin_composite_rules,
)


def test_builtin_composite_rules_have_expected_combinations() -> None:
    rules = builtin_composite_rules()

    combinations = {tuple(rule.nodes) for rule in rules}

    assert combinations == {
        ("Django", "PostgreSQL"),
        ("Docker", "PostgreSQL"),
        ("Django", "Docker"),
        ("Django", "PostgreSQL", "Docker"),
    }


def test_builtin_composite_rules_have_unique_observation_codes() -> None:
    rules = builtin_composite_rules()

    codes = [rule.observation.code for rule in rules]

    assert len(codes) == len(set(codes))


def test_builtin_composite_rules_have_observations() -> None:
    rules = builtin_composite_rules()

    assert all(rule.observation.code for rule in rules)
    assert all(rule.observation.title for rule in rules)
    assert all(rule.observation.description for rule in rules)
