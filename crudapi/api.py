from fastapi import FastAPI

from crudapi.core.config import Config
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
