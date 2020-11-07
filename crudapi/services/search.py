from crudapi.core.exceptions import NotFound
from crudapi.core.logging import logger


class SearchService:
    def __init__(self, model):
        self.model = model

    def get_one(self, db, id, *args, **kwargs):
        instance = db.query(self.model).get(id)
        if not instance:
            message = f"Couldn't find {self.model.name()} with id {id}"
            logger.warning(message)
            raise NotFound(message)
        return instance

    def get_all(self, db, *args, **kwargs):
        return db.query(self.model).all()
