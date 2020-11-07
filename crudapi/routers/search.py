from fastapi import Depends
from fastapi.routing import APIRouter

from crudapi.core.dependencies import db
from crudapi.services.search import SearchService


class SearchRouter(APIRouter):
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = SearchService(model)
        self.map_get_all()
        self.map_get_one()

    def map_get_all(self):
        self.add_api_route(path="/", methods={"GET"}, endpoint=self.get_all)

    def map_get_one(self):
        self.add_api_route(path="/{id}", methods={"GET"}, endpoint=self.get_one)

    def get_all(self, db=Depends(db)):
        """ """
        return self.service.get_all(db)

    def get_one(self, id: str, db=Depends(db)):
        """ """
        return self.service.get_one(db, id)
