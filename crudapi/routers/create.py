from http import HTTPStatus

from fastapi import Depends
from fastapi.routing import APIRouter

from crudapi.core.dependencies import db
from crudapi.services import CreateService


class CreateRouter(APIRouter):
    """Augmented API Router with methods for generating default routes."""

    def map_routes(self, orm_model, create_model, response_model):
        self.service = CreateService(orm_model)
        self.map_create(create_model, response_model)

    def map_create(self, create_model, response_model):
        """ """
        self.add_api_route(
            path="",
            methods={"POST"},
            endpoint=self.create(create_model),
            response_model=response_model,
            status_code=HTTPStatus.CREATED,
            summary="Create an instance.",
        )

    def create(self, create_model):
        """ """

        def _create(model: create_model, db=Depends(db)):
            """Create an instance."""
            return self.service.create(db, model)

        return _create
