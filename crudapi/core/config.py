from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings
from pydantic import Field

from crudapi.core.types import QueryLimit
from crudapi.core.types import QueryOffset


class DatabaseConfig(BaseSettings):

    url: str = Field("sqlite:///tests/test.db?check_same_thread=false", env="DB_DSN")
    pool_size: Optional[int] = Field(None, env="DB_POOL_SIZE")
    pool_overflow: Optional[int] = Field(None, env="DB_POOL_OVERFLOW")


class Config(BaseSettings):

    LOG_LEVEL: str = "INFO"
    DB: DatabaseConfig = DatabaseConfig()
    DEFAULT_LIMIT: QueryLimit = 10
    DEFAULT_OFFSET: QueryOffset = 0


@lru_cache()
def load_settings() -> Config:
    config = Config()
    return config


settings = load_settings()
