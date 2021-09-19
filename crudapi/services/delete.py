from sqlalchemy.orm import Session

from crudapi.core.logging import logger


class DeleteService:
    def __init__(self, model):
        self.model = model

    def delete(self, db: Session, instance, *args, **kwargs):
        """ """
        db.delete(instance)
        db.flush()
        logger.info(f"Deleted {instance}")
        return instance
