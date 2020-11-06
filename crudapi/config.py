from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings


class Config(BaseSettings):

    DB_DSN: Optional[str] = "sqlite://"


@lru_cache()
def load_settings() -> Config:
    config = Config()
    return config


settings = load_settings()
