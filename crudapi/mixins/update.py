from ..models import UpdateModel
from ..routers import UpdateRouter
from .base import router_extras


class UpdateMixin:
    def update_router(
        self,
        orm_model,
        update_model=None,
        replace_model=None,
        response_model=None,
        **kwargs
    ):
        """Include a default update router.

        Override this method if custom behavior is required.
        """
        response_model = response_model or orm_model
        replace_model = replace_model or response_model
        update_model = update_model or UpdateModel(replace_model)
        extras = router_extras(orm_model, **kwargs)
        update = UpdateRouter()
        update.map_routes(
            orm_model=orm_model,
            response_model=response_model,
            update_model=update_model,
            replace_model=replace_model,
        )
        self.include_router(update, **extras)
        return update
