from ..routers import DeleteRouter
from .base import router_extras
from crudapi.core.dependencies import db as default_db
from crudapi.services import DeleteService
from crudapi.services import SearchService


class DeleteMixin:
    def delete_router(
        self,
        orm_model,
        response_model=None,
        db=default_db,
        search_service=None,
        delete_service=None,
        **kwargs
    ):
        """Include a default delete router.

        Override this method if custom behavior is required.
        """
        response_model = response_model or orm_model
        search_service = SearchService(orm_model)
        delete_service = DeleteService(orm_model)
        delete = DeleteRouter()
        delete.map_routes(
            response_model=response_model,
            db=db,
            search_service=search_service,
            delete_service=delete_service,
        )
        extras = router_extras(orm_model, **kwargs)
        self.include_router(delete, **extras)
        return delete
