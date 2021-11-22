from ..routers import CreateRouter
from .base import router_extras
from crudapi.core.dependencies import db as default_db
from crudapi.services.create import CreateService


class CreateMixin:
    def create_router(
        self,
        orm_model,
        create_model=None,
        response_model=None,
        db=default_db,
        service=None,
        **kwargs
    ):
        """Include a default create router.

        Override this method if custom behavior is required.
        """
        response_model = response_model or orm_model
        create_model = create_model or response_model
        service = service or CreateService(orm_model)
        create = CreateRouter()
        extras = router_extras(orm_model, **kwargs)
        create.map_routes(
            response_model=response_model,
            create_model=create_model,
            db=db,
            service=service,
        )
        self.include_router(create, **extras)
        return create
