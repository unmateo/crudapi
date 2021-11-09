from fastapi import FastAPI

from crudapi.models import UpdateModel
from crudapi.routers import CreateRouter
from crudapi.routers import DeleteRouter
from crudapi.routers import SearchRouter
from crudapi.routers import UpdateRouter


class CrudAPI(FastAPI):
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
        self.crudapi_routers = {}
        self.search_router(
            orm_model=orm_model, response_model=response_model, **commons
        )
        self.create_router(
            orm_model=orm_model,
            response_model=response_model,
            create_model=create_model or response_model,
            **commons,
        )
        self.update_router(
            orm_model=orm_model,
            response_model=response_model,
            update_model=update_model or UpdateModel(create_model),
            replace_model=create_model,
            **commons,
        )
        self.delete_router(
            orm_model=orm_model, response_model=response_model, **commons
        )

    def search_router(self, orm_model, response_model, **kwargs):
        """Include a default search router.

        Override this method if custom behavior is required.
        """
        search = SearchRouter()
        search.map_routes(orm_model=orm_model, response_model=response_model)
        self.include_router(search, **kwargs)
        self.crudapi_routers["search"] = search
        return search

    def create_router(self, orm_model, create_model, response_model, **kwargs):
        """Include a default create router.

        Override this method if custom behavior is required.
        """
        create = CreateRouter()
        create.map_routes(
            orm_model=orm_model,
            response_model=response_model,
            create_model=create_model,
        )
        self.include_router(create, **kwargs)
        self.crudapi_routers["create"] = create
        return create

    def update_router(
        self, orm_model, update_model, replace_model, response_model, **kwargs
    ):
        """Include a default update router.

        Override this method if custom behavior is required.
        """
        update = UpdateRouter()
        update.map_routes(
            orm_model=orm_model,
            response_model=response_model,
            update_model=update_model,
            replace_model=replace_model,
        )
        self.include_router(update, **kwargs)
        self.crudapi_routers["update"] = update
        return update

    def delete_router(self, orm_model, response_model, **kwargs):
        """Include a default delete router.

        Override this method if custom behavior is required.
        """
        delete = DeleteRouter()
        delete.map_routes(orm_model=orm_model, response_model=response_model)
        self.include_router(delete, **kwargs)
        self.crudapi_routers["delete"] = delete
        return delete
