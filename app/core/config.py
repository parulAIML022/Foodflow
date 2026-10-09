from pathlib import Path 
from pydantic_settings import BaseSettings, SettingsConfigDict
BASE_DIR = Path(__file__).resolve().parents[2]
class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore"
    )
settings = Settings()