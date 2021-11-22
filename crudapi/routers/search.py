from typing import List

from fastapi import APIRouter
from fastapi import Depends

from crudapi.core.paginator import BasePaginator


class SearchRouter(APIRouter):
    """Augmented API Router with methods for generating default routes."""

    def map_routes(self, response_model, db, search_service):
        self.map_get_all(
            response_model=response_model, search_service=search_service, db=db
        )
        self.map_get_one(
            response_model=response_model, search_service=search_service, db=db
        )

    def map_get_all(self, response_model, search_service, db):
        self.add_api_route(
            path="",
            methods={"GET"},
            endpoint=self._get_all(search_service, db),
            response_model=List[response_model],
            summary="Retrieve all instances.",
        )

    def map_get_one(self, response_model, search_service, db):
        self.add_api_route(
            path="/{id}",
            methods={"GET"},
            endpoint=self._get_one(search_service, db),
            response_model=response_model,
            summary="Retrieve one instance.",
        )

    def _get_all(self, search_service, db):
        def get_all(paginator: BasePaginator = Depends(), session=Depends(db)):
            """Retrieve all instances with pagination."""
            resources = search_service.get_all(session, paginator)
            return resources

        return get_all

    def _get_one(self, search_service, db):
        def get_one(id: str, session=Depends(db)):
            """Retrieve an instance."""
            return search_service.get_one(session, id)

        return get_one
