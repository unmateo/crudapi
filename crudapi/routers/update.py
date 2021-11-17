from fastapi import Depends
from fastapi.routing import APIRouter

from crudapi.core.dependencies import db
from crudapi.services import SearchService
from crudapi.services import UpdateService


class UpdateRouter(APIRouter):
    """Augmented API Router with methods for generating default routes."""

    def map_routes(self, orm_model, update_model, replace_model, response_model):
        self.search_service = SearchService(orm_model)
        self.update_service = UpdateService(orm_model)
        self.map_patch(update_model, response_model)
        self.map_put(replace_model)

    def map_patch(self, update_model, response_model):
        """ """
        self.add_api_route(
            path="/{id}",
            methods={"PATCH"},
            endpoint=self.patch(update_model),
            response_model=response_model,
            summary="Update an instance.",
        )

    def map_put(self, replace_model):
        """ """
        self.add_api_route(
            path="/{id}",
            methods={"PUT"},
            endpoint=self.put(replace_model),
            summary="Replace an instance.",
        )

    def patch(self, update_model):
        """Update an instance."""

        def _patch(id: str, fields: update_model, db=Depends(db)):
            instance = self.search_service.get_one(db, id)
            return self.update_service.update(
                db, instance, fields.dict(exclude_unset=True)
            )

        return _patch

    def put(self, replace_model):
        """Replace an instance."""

        def _put(id: str, fields: replace_model, db=Depends(db)):
            instance = self.search_service.get_one(db, id)
            exclusions = {
                "id": ...,
                "created_at": ...,
                "updated_at": ...,
            }
            return self.update_service.update(
                db, instance, fields.dict(exclude=exclusions)
            )

        return _put
