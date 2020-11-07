from fastapi.routing import APIRouter

from crudapi.config import settings
from crudapi.services.search import SearchService


class SearchRouter(APIRouter):

    service = SearchService(model=settings.MODEL)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.map_get_all()
        self.map_get_one()

    def map_get_all(self):
        self.add_api_route(path="/", methods={"GET"}, endpoint=self.get_all)

    def map_get_one(self):
        self.add_api_route(path="/{id}", methods={"GET"}, endpoint=self.get_one)

    @classmethod
    def get_all(cls):
        """ """
        return cls.service.get_all()

    @classmethod
    def get_one(cls, id: str):
        """ """
        return cls.service.get_one(id)
