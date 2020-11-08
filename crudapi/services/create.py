from crudapi.core.logging import logger


class CreateService:
    def __init__(self, model):
        self.model = model

    def create(self, db, model, *args, **kwargs):
        instance = self.model(**model.dict())
        db.add(instance)
        db.flush()
        return instance
