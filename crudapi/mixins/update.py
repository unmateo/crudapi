from ..models import UpdateModel
from ..routers import UpdateRouter
from .base import router_extras
from crudapi.core.dependencies import db as default_db
from crudapi.services import SearchService
from crudapi.services import UpdateService


class UpdateMixin:
    def update_router(
        self,
        orm_model,
        update_model=None,
        replace_model=None,
        response_model=None,
        db=default_db,
        search_service=None,
        update_service=None,
        **kwargs
    ):
        """Include a default update router.

        Override this method if custom behavior is required.
        """
        response_model = response_model or orm_model
        replace_model = replace_model or response_model
        update_model = update_model or UpdateModel(replace_model)
        search_service = search_service or SearchService(orm_model)
        update_service = update_service or UpdateService(orm_model)
        update = UpdateRouter()
        update.map_routes(
            response_model=response_model,
            update_model=update_model,
            replace_model=replace_model,
            db=db,
            search_service=search_service,
            update_service=update_service,
        )
        extras = router_extras(orm_model, **kwargs)
        self.include_router(update, **extras)
        return update
