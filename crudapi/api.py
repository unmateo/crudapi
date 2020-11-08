from fastapi import FastAPI

from crudapi.core.config import Config
from crudapi.routers.create import CreateRouter
from crudapi.routers.delete import DeleteRouter
from crudapi.routers.search import SearchRouter


class CrudAPI(FastAPI):
    def __init__(
        self,
        orm_model,
        api_model,
        prefix: str = "/",
        config: Config = Config(),
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.include_router(
            SearchRouter(orm_model=orm_model, api_model=api_model), prefix=prefix
        )
        self.include_router(
            CreateRouter(orm_model=orm_model, api_model=api_model), prefix=prefix
        )
        self.include_router(
            DeleteRouter(orm_model=orm_model, api_model=api_model), prefix=prefix
        )
