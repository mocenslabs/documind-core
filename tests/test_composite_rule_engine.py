from app.application.inference.composite_rule_engine import (
    CompositeInferenceRuleEngine,
)
from app.domain.inference.category import (
    ObservationCategory,
)
from app.domain.inference.composite_rules import (
    CompositeInferenceRule,
)
from app.domain.inference.confidence import Confidence
from app.domain.inference.entities import Observation
from app.domain.inference.priority import Priority
from app.domain.inference.severity import Severity
from app.domain.knowledge.graph import KnowledgeGraph


def test_composite_rule() -> None:
    graph = KnowledgeGraph()

    graph.add_node("Django")
    graph.add_node("PostgreSQL")

    engine = CompositeInferenceRuleEngine(
        (
            CompositeInferenceRule(
                nodes=(
                    "Django",
                    "PostgreSQL",
                ),
                observation=Observation(
                    code="demo",
                    title="Demo",
                    description="Demo",
                    severity=Severity.INFO,
                    priority=Priority.LOW,
                    category=ObservationCategory.GENERAL,
                    confidence=Confidence.CERTAIN,
                ),
            ),
        )
    )

    result = engine.evaluate(graph)

    assert len(result) == 1
