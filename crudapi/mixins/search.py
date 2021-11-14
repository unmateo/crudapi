from ..routers.search import SearchRouter


class SearchMixin:
    def search_router(self, orm_model, response_model, **kwargs):
        """Include a default search router.

        Override this method if custom behavior is required.
        """
        search = SearchRouter()
        search.map_routes(orm_model=orm_model, response_model=response_model)
        self.include_router(search, **kwargs)
        self.crudapi_routers["search"] = search
        return search
