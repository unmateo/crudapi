from fastapi import FastAPI

from .core.dependencies import db as default_db
from .mixins import CreateMixin
from .mixins import DeleteMixin
from .mixins import SearchMixin
from .mixins import UpdateMixin
from crudapi.services import CreateService
from crudapi.services import DeleteService
from crudapi.services import SearchService
from crudapi.services import UpdateService


class CrudAPI(FastAPI, SearchMixin, UpdateMixin, CreateMixin, DeleteMixin):
    """Extends FastAPI adding methods for reasonable default behavior."""

    def include_model(
        self,
        orm_model,
        response_model=None,
        create_model=None,
        update_model=None,
        db=default_db,
        search_service=None,
        create_service=None,
        update_service=None,
        delete_service=None,
    ):
        if self.title == "FastAPI":
            self.title = orm_model.__tablename__.capitalize()

        search_service = search_service or SearchService(orm_model)
        create_service = create_service or CreateService(orm_model)
        update_service = update_service or UpdateService(orm_model)
        delete_service = delete_service or DeleteService(orm_model)

        self.search_router(
            orm_model=orm_model,
            response_model=response_model,
            db=db,
            search_service=search_service,
        )

        self.create_router(
            orm_model=orm_model,
            response_model=response_model,
            db=db,
            create_model=create_model,
        )

        self.update_router(
            orm_model=orm_model,
            response_model=response_model,
            update_model=update_model,
            replace_model=create_model,
            db=db,
            search_service=search_service,
            update_service=update_service,
        )

        self.delete_router(
            orm_model=orm_model,
            response_model=response_model,
            db=db,
            search_service=search_service,
            delete_service=delete_service,
        )
