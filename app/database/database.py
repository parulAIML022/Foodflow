from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    DATABASE_URL : str
    model_config = SettingsConfigDict(
        env_file = ".env",
        extra= "ignore"
    )
settings = Settings()
engine = create_engine(
        settings.DATABASE_URL
    )
SessionLocal = sessionmaker(
        bind=engine,
        autocommit = False,
        autoflush=False
    )
Base = declarative_base()
def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()