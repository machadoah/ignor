from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=True,
    )

    # Path to the gitignore templates
    TEMPLATES_PATH: Path = Path(__file__).parent.parent / 'templates'

    # GROQ settings
    GROQ_API_KEY: str = 'secret-key'
