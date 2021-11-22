from fastapi import Depends
from fastapi.routing import APIRouter


class UpdateRouter(APIRouter):
    """Augmented API Router with methods for generating default routes."""

    def map_routes(
        self,
        update_model,
        replace_model,
        response_model,
        db,
        search_service,
        update_service,
    ):
        self.map_patch(update_model, response_model, db, search_service, update_service)
        self.map_put(replace_model, db, search_service, update_service)

    def map_patch(
        self, update_model, response_model, db, search_service, update_service
    ):
        """ """
        patch_endpoint = self._patch(
            update_model=update_model,
            db=db,
            search_service=search_service,
            update_service=update_service,
        )
        self.add_api_route(
            path="/{id}",
            methods={"PATCH"},
            endpoint=patch_endpoint,
            response_model=response_model,
            summary="Update an instance.",
        )

    def map_put(self, replace_model, db, search_service, update_service):
        """ """
        put_endpoint = self._put(
            replace_model=replace_model,
            db=db,
            search_service=search_service,
            update_service=update_service,
        )
        self.add_api_route(
            path="/{id}",
            methods={"PUT"},
            endpoint=put_endpoint,
            summary="Replace an instance.",
        )

    def _patch(self, update_model, db, search_service, update_service):
        def patch(id: str, fields: update_model, session=Depends(db)):
            """Update an instance."""
            instance = search_service.get_one(session, id)
            return update_service.update(
                session, instance, fields.dict(exclude_unset=True)
            )

        return patch

    def _put(self, replace_model, db, search_service, update_service):
        def put(id: str, fields: replace_model, session=Depends(db)):
            """Replace an instance."""

            instance = search_service.get_one(session, id)
            exclusions = {
                "id": ...,
                "created_at": ...,
                "updated_at": ...,
            }
            return update_service.update(
                session, instance, fields.dict(exclude=exclusions)
            )

        return put
