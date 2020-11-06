class SearchService:
    def get_one(self, id, *args, **kwargs):
        raise NotImplementedError()

    def get_all(self, *args, **kwargs):
        raise NotImplementedError()

    def get_by_filter(self, *args, **kwargs):
        raise NotImplementedError()
