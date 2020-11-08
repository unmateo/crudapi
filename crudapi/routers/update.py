from fastapi import Depends
from fastapi.routing import APIRouter

from crudapi.core.dependencies import db
from crudapi.services.search import SearchService
from crudapi.services.update import UpdateService


class UpdateRouter(APIRouter):
    def __init__(self, orm_model, api_model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.search_service = SearchService(orm_model)
        self.update_service = UpdateService(orm_model)
        self.map_patch(api_model)

    def map_patch(self, api_model):
        """ """
        self.add_api_route(
            path="/{id}",
            methods={"PATCH"},
            endpoint=self.patch(api_model),
            response_model=api_model,
        )

    def patch(self, api_model):
        """ """

        def _patch(id: str, fields: api_model, db=Depends(db)):
            instance = self.search_service.get_one(db, id)
            return self.update_service.update(
                db, instance, fields.dict(exclude_unset=True)
            )

        return _patch
