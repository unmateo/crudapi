from fastapi import FastAPI

from .mixins import CreateMixin
from .mixins import DeleteMixin
from .mixins import SearchMixin
from .mixins import UpdateMixin
from .models import UpdateModel


class CrudAPI(FastAPI, SearchMixin, UpdateMixin, CreateMixin, DeleteMixin):
    """Extends FastAPI adding methods for reasonable default behavior."""

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
        self.search_router(
            orm_model=orm_model, response_model=response_model, **commons
        )
        self.create_router(
            orm_model=orm_model,
            response_model=response_model,
            create_model=create_model,
            **commons,
        )
        self.update_router(
            orm_model=orm_model,
            response_model=response_model,
            update_model=update_model,
            replace_model=create_model,
            **commons,
        )
        self.delete_router(
            orm_model=orm_model, response_model=response_model, **commons
        )
