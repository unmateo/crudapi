from ..routers import CreateRouter


class CreateMixin:
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
