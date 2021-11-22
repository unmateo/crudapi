from http import HTTPStatus

from fastapi import Depends
from fastapi.routing import APIRouter


class CreateRouter(APIRouter):
    """Augmented API Router with methods for generating default routes."""

    def map_routes(self, create_model, response_model, db, create_service):
        self.map_create(create_model, response_model, db, create_service)

    def map_create(self, create_model, response_model, db, create_service):
        """ """
        creator = self._create(
            create_model=create_model,
            db=db,
            create_service=create_service,
        )
        self.add_api_route(
            path="",
            methods={"POST"},
            endpoint=creator,
            response_model=response_model,
            status_code=HTTPStatus.CREATED,
            summary="Create an instance.",
        )

    def _create(self, create_model, db, create_service):
        def create(model: create_model, session=Depends(db)):
            """Create an instance."""
            instance = create_service.create(session, model)
            return instance

        return create
