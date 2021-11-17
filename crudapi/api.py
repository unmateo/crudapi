from fastapi import FastAPI

from .mixins import CreateMixin
from .mixins import DeleteMixin
from .mixins import SearchMixin
from .mixins import UpdateMixin


class CrudAPI(FastAPI, SearchMixin, UpdateMixin, CreateMixin, DeleteMixin):
    """Extends FastAPI adding methods for reasonable default behavior."""

    def include_model(
        self,
        orm_model,
        response_model=None,
        create_model=None,
        update_model=None,
    ):
        if self.title == "FastAPI":
            self.title = orm_model.__tablename__.capitalize()

        self.search_router(
            orm_model=orm_model,
            response_model=response_model,
        )
        self.create_router(
            orm_model=orm_model,
            response_model=response_model,
            create_model=create_model,
        )
        self.update_router(
            orm_model=orm_model,
            response_model=response_model,
            update_model=update_model,
            replace_model=create_model,
        )
        self.delete_router(
            orm_model=orm_model,
            response_model=response_model,
        )
