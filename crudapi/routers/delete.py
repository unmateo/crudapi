from fastapi import Depends
from fastapi.routing import APIRouter


class DeleteRouter(APIRouter):
    """Augmented API Router with methods for generating default routes."""

    def map_routes(
        self,
        response_model,
        db,
        search_service,
        delete_service,
    ):
        self.map_delete(response_model, db, search_service, delete_service)

    def map_delete(self, response_model, db, search_service, delete_service):
        """ """
        delete_endpoint = self._delete(
            db=db,
            search_service=search_service,
            delete_service=delete_service,
        )
        self.add_api_route(
            path="/{id}",
            methods={"DELETE"},
            endpoint=delete_endpoint,
            response_model=response_model,
            summary="Delete an instance.",
        )

    def _delete(self, db, search_service, delete_service):
        def delete(id: str, session=Depends(db)):
            """Delete an instance."""
            instance = search_service.get_one(session, id)
            return delete_service.delete(session, instance)

        return delete
