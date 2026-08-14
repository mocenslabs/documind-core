"""Application composition root."""

from app.application.analyze.service import AnalyzeRepositoryService
from app.application.discovery.service import DiscoveryService
from app.application.inference.service import InferenceService
from app.application.knowledge.graph_builder import KnowledgeGraphBuilder
from app.application.knowledge.registry_service import KnowledgeRegistryService
from app.application.knowledge.relationship_builder import (
    KnowledgeRelationshipBuilder,
)
from app.application.knowledge.service import (
    KnowledgeExtractionService,
    KnowledgeService,
)
from app.application.parser.service import ParserService
from app.application.recommendation.rule_engine import RecommendationRuleEngine
from app.application.recommendation.service import RecommendationService
from app.application.rules.builtin_rules import builtin_rules
from app.application.rules.service import RuleEngineService
from app.application.scanner.service import ScannerService
from app.infrastructure.inference.local_engine import LocalInferenceEngine
from app.infrastructure.knowledge.local_extractor import LocalKnowledgeExtractor
from app.infrastructure.parser.local_parser import LocalParser
from app.infrastructure.repository_loader.local_loader import (
    LocalRepositoryLoader,
)
from app.infrastructure.scanner.local_scanner import LocalScanner


def create_analyzer() -> AnalyzeRepositoryService:
    """Create the fully configured repository analysis service."""

    loader = LocalRepositoryLoader()

    scanner_service = ScannerService(
        scanner=LocalScanner(),
    )

    parser_service = ParserService(
        parser=LocalParser(),
    )

    rule_engine = RuleEngineService(
        rules=builtin_rules(),
    )

    knowledge_service = KnowledgeService(
        rule_engine=rule_engine,
    )

    knowledge_extraction_service = KnowledgeExtractionService(
        extractor=LocalKnowledgeExtractor(),
    )

    knowledge_registry_service = KnowledgeRegistryService()

    knowledge_relationship_builder = KnowledgeRelationshipBuilder()

    knowledge_graph_builder = KnowledgeGraphBuilder()

    inference_service = InferenceService(
        engine=LocalInferenceEngine(),
    )

    recommendation_service = RecommendationService(
        engine=RecommendationRuleEngine(),
    )

    return AnalyzeRepositoryService(
        repository_loader=loader,
        scanner_service=scanner_service,
        parser_service=parser_service,
        discovery_service=DiscoveryService(),
        knowledge_service=knowledge_service,
        knowledge_extraction_service=knowledge_extraction_service,
        knowledge_registry_service=knowledge_registry_service,
        knowledge_relationship_builder=knowledge_relationship_builder,
        knowledge_graph_builder=knowledge_graph_builder,
        inference_service=inference_service,
        recommendation_service=recommendation_service,
    )
