from fastapi import FastAPI

from crudapi.config import Config
from crudapi.routers.search import SearchRouter


class CrudAPI(FastAPI):
    def __init__(self, prefix: str = "/", config: Config = Config(), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.include_router(SearchRouter(), prefix=prefix)
