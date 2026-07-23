"""Structured logging configuration."""

import logging

import structlog

from app.core.config.settings import settings


def configure_logging() -> None:
    """Configure structured logging for the application process."""
    log_level = logging.getLevelNamesMapping()[settings.log_level]
    logging.basicConfig(level=log_level, format="%(message)s")
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(log_level),
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )
