from fastapi import Depends
from fastapi.routing import APIRouter

from crudapi.core.dependencies import db
from crudapi.services.create import CreateService


class CreateRouter(APIRouter):
    def __init__(self, orm_model, api_model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = CreateService(orm_model)
        self.map_create(api_model)

    def map_create(self, api_model):
        """ """
        self.add_api_route(path="", methods={"POST"}, endpoint=self.create(api_model))

    def create(self, api_model):
        """ """

        def _create(model: api_model, db=Depends(db)):
            """ """
            return self.service.create(db, model)

        return _create
