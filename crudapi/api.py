from fastapi import FastAPI

from crudapi.core.models import update
from crudapi.routers.create import CreateRouter
from crudapi.routers.delete import DeleteRouter
from crudapi.routers.search import SearchRouter
from crudapi.routers.update import UpdateRouter


class CrudAPI(FastAPI):
    def __init__(self, orm_model, api_model, prefix: str = "/", *args, **kwargs):
        super().__init__(*args, **kwargs)
        commons = {
            "prefix": prefix,
            "tags": [kwargs.get("title", "default")],
        }
        self.include_router(
            SearchRouter(orm_model=orm_model, api_model=api_model), **commons
        )
        self.include_router(
            CreateRouter(orm_model=orm_model, api_model=api_model), **commons
        )
        self.include_router(
            DeleteRouter(orm_model=orm_model, api_model=api_model), **commons
        )
        self.include_router(
            UpdateRouter(orm_model=orm_model, api_model=update(api_model)),
            **commons,
        )
