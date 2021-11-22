from ..routers.search import SearchRouter
from .base import router_extras
from crudapi.core.dependencies import db as default_db


class SearchMixin:
    def search_router(self, orm_model, response_model=None, db=default_db, **kwargs):
        """Include a default search router.

        Override this method if custom behavior is required.
        """
        response_model = response_model or orm_model
        extras = router_extras(orm_model, **kwargs)
        search = SearchRouter()
        search.map_routes(orm_model=orm_model, response_model=response_model, db=db)
        self.include_router(search, **extras)
        return search
