from typing import List

from fastapi import APIRouter
from fastapi import Depends

from crudapi.core.paginator import BasePaginator
from crudapi.services import SearchService


class SearchRouter(APIRouter):
    """Augmented API Router with methods for generating default routes."""

    def map_routes(self, orm_model, response_model, db):
        service = SearchService(orm_model)
        self.map_get_all(response_model=response_model, service=service, db=db)
        self.map_get_one(response_model=response_model, service=service, db=db)

    def map_get_all(self, response_model, service, db):
        self.add_api_route(
            path="",
            methods={"GET"},
            endpoint=self._get_all(service, db),
            response_model=List[response_model],
            summary="Retrieve all instances.",
        )

    def map_get_one(self, response_model, service, db):
        self.add_api_route(
            path="/{id}",
            methods={"GET"},
            endpoint=self._get_one(service, db),
            response_model=response_model,
            summary="Retrieve one instance.",
        )

    def _get_all(self, service, db):
        def get_all(paginator: BasePaginator = Depends(), session=Depends(db)):
            """Retrieve all instances with pagination."""
            resources = service.get_all(session, paginator)
            return resources

        return get_all

    def _get_one(self, service, db):
        def get_one(id: str, session=Depends(db)):
            """Retrieve an instance."""
            return service.get_one(session, id)

        return get_one
