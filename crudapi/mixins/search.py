from ..routers.search import SearchRouter
from .base import router_extras
from crudapi.core.dependencies import db as default_db
from crudapi.services import SearchService


class SearchMixin:
    def search_router(
        self, orm_model, response_model=None, db=default_db, service=None, **kwargs
    ):
        """Include a default search router.

        Override this method if custom behavior is required.
        """
        response_model = response_model or orm_model
        service = service or SearchService(orm_model)
        search = SearchRouter()
        extras = router_extras(orm_model, **kwargs)
        search.map_routes(response_model=response_model, db=db, service=service)
        self.include_router(search, **extras)
        return search
