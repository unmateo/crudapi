from typing import List

from fastapi import APIRouter
from fastapi import Depends

from crudapi.core.dependencies import db
from crudapi.core.paginator import BasePaginator
from crudapi.services import SearchService


class SearchRouter(APIRouter):
    """Augmented API Router with methods for generating default routes."""

    def map_routes(self, orm_model, response_model):
        self.service = SearchService(orm_model)
        self.map_get_all(response_model=response_model)
        self.map_get_one(response_model=response_model)

    def map_get_all(self, response_model):
        self.add_api_route(
            path="",
            methods={"GET"},
            endpoint=self.get_all,
            response_model=List[response_model],
            summary="Retrieve all instances.",
        )

    def map_get_one(self, response_model):
        self.add_api_route(
            path="/{id}",
            methods={"GET"},
            endpoint=self.get_one,
            response_model=response_model,
            summary="Retrieve one instance.",
        )

    def get_all(self, paginator: BasePaginator = Depends(), db=Depends(db)):
        """Retrieve all instances with pagination."""
        resources = self.service.get_all(db, paginator)
        return resources

    def get_one(self, id: str, db=Depends(db)):
        """Retrieve an instance."""
        return self.service.get_one(db, id)
