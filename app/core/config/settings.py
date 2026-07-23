"""Configuration loaded from the execution environment."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings sourced from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="DOCUMIND_",
        extra="ignore",
    )

    log_level: str = "INFO"


settings = Settings()
