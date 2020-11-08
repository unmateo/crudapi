from fastapi import FastAPI

from crudapi.core.models import Update
from crudapi.routers.create import CreateRouter
from crudapi.routers.delete import DeleteRouter
from crudapi.routers.search import SearchRouter
from crudapi.routers.update import UpdateRouter


class CrudAPI(FastAPI):
    def __init__(
        self,
        orm_model,
        response_model,
        create_model=None,
        update_model=None,
        prefix: str = "/",
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        commons = {
            "prefix": prefix,
            "tags": [kwargs.get("title", "default")],
        }
        create_model = create_model or response_model
        update_model = update_model or Update(create_model)
        search = SearchRouter(orm_model=orm_model, response_model=response_model)
        delete = DeleteRouter(orm_model=orm_model, response_model=response_model)
        create = CreateRouter(
            orm_model=orm_model,
            response_model=response_model,
            create_model=create_model,
        )
        update = UpdateRouter(
            orm_model=orm_model,
            response_model=response_model,
            update_model=update_model,
        )
        self.include_router(search, **commons)
        self.include_router(delete, **commons)
        self.include_router(create, **commons)
        self.include_router(update, **commons)
