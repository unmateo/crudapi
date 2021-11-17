from ..routers import UpdateRouter


class UpdateMixin:
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
        return update
