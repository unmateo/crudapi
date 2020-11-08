from typing import List

from fastapi import Depends
from fastapi.routing import APIRouter

from crudapi.core.dependencies import db
from crudapi.services.search import SearchService


class SearchRouter(APIRouter):
    def __init__(self, orm_model, api_model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = SearchService(orm_model)
        self.map_get_all(api_model=api_model)
        self.map_get_one(api_model=api_model)

    def map_get_all(self, api_model):
        self.add_api_route(
            path="/",
            methods={"GET"},
            endpoint=self.get_all,
            response_model=List[api_model],
        )

    def map_get_one(self, api_model):
        self.add_api_route(
            path="/{id}",
            methods={"GET"},
            endpoint=self.get_one,
            response_model=api_model,
        )

    def get_all(self, db=Depends(db)):
        """ """
        return self.service.get_all(db)

    def get_one(self, id: str, db=Depends(db)):
        """ """
        return self.service.get_one(db, id)
