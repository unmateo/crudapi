from fastapi import Depends
from fastapi.routing import APIRouter

from crudapi.core.dependencies import db
from crudapi.services.delete import DeleteService
from crudapi.services.search import SearchService


class DeleteRouter(APIRouter):
    def __init__(self, orm_model, api_model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.delete_service = DeleteService(orm_model)
        self.search_service = SearchService(orm_model)
        self.map_create(api_model)

    def map_create(self, api_model):
        """ """
        self.add_api_route(
            path="/{id}",
            methods={"DELETE"},
            endpoint=self.delete,
            response_model=api_model,
        )

    def delete(self, id: str, db=Depends(db)):
        """ """
        instance = self.search_service.get_one(db, id)
        return self.delete_service.delete(db, instance)
