from sqlalchemy.orm import Session

from crudapi.core.exceptions import NotFound
from crudapi.core.logging import logger
from crudapi.core.paginator import BasePaginator
from crudapi.models.base import BaseModel


class SearchService:
    def __init__(self, model: BaseModel):
        self.model = model

    def get_one(self, db, id, *args, **kwargs):
        instance = db.query(self.model).get(id)
        if not instance:
            message = f"Couldn't find {instance}"
            logger.warning(message)
            raise NotFound()
        return instance

    def get_all(
        self, db: Session, paginator: BasePaginator = BasePaginator(), *args, **kwargs
    ):
        """ """
        resources = (
            db.query(self.model)
            .order_by(self.model.created_at.desc())
            .limit(paginator.limit)
            .offset(paginator.offset)
            .all()
        )
        return resources
