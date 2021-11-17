from ..routers import DeleteRouter
from .base import router_extras


class DeleteMixin:
    def delete_router(self, orm_model, response_model=None, **kwargs):
        """Include a default delete router.

        Override this method if custom behavior is required.
        """
        response_model = response_model or orm_model
        extras = router_extras(orm_model, **kwargs)
        delete = DeleteRouter()
        delete.map_routes(orm_model=orm_model, response_model=response_model)
        self.include_router(delete, **extras)
        return delete
