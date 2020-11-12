from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings
from pydantic import Field


class DatabaseConfig(BaseSettings):

    url: str = Field("sqlite:///tests/test.db?check_same_thread=false", env="DB_DSN")
    pool_size: Optional[int] = Field(None, env="DB_POOL_SIZE")
    pool_overflow: Optional[int] = Field(None, env="DB_POOL_OVERFLOW")


class Config(BaseSettings):

    LOG_LEVEL: str = "INFO"
    DB: DatabaseConfig = DatabaseConfig()


@lru_cache()
def load_settings() -> Config:
    config = Config()
    return config


settings = load_settings()
