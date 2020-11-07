class SearchService:
    def __init__(self, model):
        self.model = model

    def get_one(self, id, *args, **kwargs):
        return {"id": "sarasa", "title": "titulo"}

    def get_all(self, *args, **kwargs):
        return [{"id": "sarasa", "title": "titulo"}]
