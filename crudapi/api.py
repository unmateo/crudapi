from fastapi import FastAPI

from crudapi.core.config import Config
from crudapi.models.default import DefaultModel
from crudapi.routers.search import SearchRouter


class CrudAPI(FastAPI):
    def __init__(
        self,
        prefix: str = "/",
        model=DefaultModel,
        config: Config = Config(),
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.include_router(SearchRouter(model=model), prefix=prefix)
