from functools import lru_cache
from typing import Callable
from typing import Optional

from pydantic import BaseSettings

from crudapi.defaults.model import Model


class Config(BaseSettings):

    DB_DSN: Optional[str] = "sqlite://"
    MODEL: Callable = Model


@lru_cache()
def load_settings() -> Config:
    config = Config()
    return config


settings = load_settings()
