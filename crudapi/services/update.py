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
