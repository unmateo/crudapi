from ..routers import DeleteRouter


class DeleteMixin:
    def delete_router(self, orm_model, response_model, **kwargs):
        """Include a default delete router.

        Override this method if custom behavior is required.
        """
        delete = DeleteRouter()
        delete.map_routes(orm_model=orm_model, response_model=response_model)
        self.include_router(delete, **kwargs)
        return delete
