from fastapi import FastAPI

from crudapi.core.database import check_connection
from crudapi.core.logging import logger
from crudapi.models.update import UpdateModel
from crudapi.routers.create import CreateRouter
from crudapi.routers.delete import DeleteRouter
from crudapi.routers.search import SearchRouter
from crudapi.routers.update import UpdateRouter


class CrudAPI(FastAPI):
    def __init__(
        self,
        orm_model,
        response_model=None,
        create_model=None,
        update_model=None,
        prefix: str = None,
        *args,
        **kwargs,
    ):
        table = orm_model.__tablename__.capitalize()
        title = kwargs.pop("title", None) or table
        super().__init__(*args, title=title, **kwargs)
        prefix = prefix or f"/{orm_model.__tablename__}"
        response_model = response_model or orm_model
        commons = {
            "prefix": prefix,
            "tags": [table],
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
        self.add_event_handler("startup", check_connection)
        logger.info("app started")
