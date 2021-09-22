from crudapi.core.exceptions import NotFound
from crudapi.core.logging import logger


class UpdateService:
    def __init__(self, model):
        self.model = model

    def update(self, db, instance, fields, *args, **kwargs):
        """ """
        for key, value in fields.items():
            setattr(instance, key, value)
        db.flush()
        db.refresh(instance)
        logger.info(f"Updated {instance}")
        return instance

    def put(self, db, id, fields, *args, **kwargs) -> int:
        """ """
        updated = db.query(self.model).filter_by(id=id).update(fields)
        if updated == 0:
            raise NotFound()
        logger.info(f"Replaced <{id}> {fields}")
        return updated
