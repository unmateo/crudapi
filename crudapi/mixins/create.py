from ..routers import CreateRouter
from .base import router_extras


class CreateMixin:
    def create_router(
        self, orm_model, create_model=None, response_model=None, **kwargs
    ):
        """Include a default create router.

        Override this method if custom behavior is required.
        """
        response_model = response_model or orm_model
        create_model = create_model or response_model
        extras = router_extras(orm_model, **kwargs)
        create = CreateRouter()
        create.map_routes(
            orm_model=orm_model,
            response_model=response_model,
            create_model=create_model,
        )
        self.include_router(create, **extras)
        return create
