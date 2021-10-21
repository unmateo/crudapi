from fastapi import FastAPI

from crudapi.models.update import UpdateModel
from crudapi.routers.create import CreateRouter
from crudapi.routers.delete import DeleteRouter
from crudapi.routers.search import SearchRouter
from crudapi.routers.update import UpdateRouter


class CrudAPI(FastAPI):
    def include_model(
        self,
        orm_model,
        response_model=None,
        create_model=None,
        update_model=None,
    ):
        table = orm_model.__tablename__
        title = table.capitalize()
        if self.title == "FastAPI":
            self.title = title
        response_model = response_model or orm_model
        commons = {
            "prefix": f"/{table}",
            "tags": [title],
        }
        create_model = create_model or response_model
        update_model = update_model or UpdateModel(create_model)
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
            create_model=create_model,
        )
        self.include_router(search, **commons)
        self.include_router(delete, **commons)
        self.include_router(create, **commons)
        self.include_router(update, **commons)
