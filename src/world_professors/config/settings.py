"""Application settings management."""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Data directories
    data_dir: Path = Path("data")
    wiki_output_dir: Path = Path("wiki")

    # Logging configuration
    log_level: str = "INFO"
    log_file: Path | None = None

    # AI API keys (optional)
    openai_api_key: str | None = None
    anthropic_api_key: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    def __init__(self, **kwargs):  # type: ignore[no-untyped-def]
        """Initialize settings."""
        super().__init__(**kwargs)

        # Ensure directories are absolute paths
        if not self.data_dir.is_absolute():
            self.data_dir = Path.cwd() / self.data_dir
        if not self.wiki_output_dir.is_absolute():
            self.wiki_output_dir = Path.cwd() / self.wiki_output_dir


# Global settings instance
settings = Settings()  # type: ignore[no-untyped-call]
