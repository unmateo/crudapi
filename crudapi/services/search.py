from sqlalchemy.orm import Session

from crudapi.core.exceptions import NotFound
from crudapi.core.logging import logger
from crudapi.core.paginator import BasePaginator
from crudapi.models.orm import BaseORM


class SearchService:
    def __init__(self, model: BaseORM):
        self.model = model

    def get_one(self, db, id, *args, **kwargs):
        instance = db.query(self.model).get(id)
        if not instance:
            message = f"Couldn't find {self.model.name()} with id {id}"
            logger.warning(message)
            raise NotFound()
        return instance

    def get_all(
        self, db: Session, paginator: BasePaginator = BasePaginator(), *args, **kwargs
    ):
        """ """
        resources = (
            db.query(self.model)
            .order_by(self.model.created.desc())
            .limit(paginator.limit)
            .offset(paginator.offset)
            .all()
        )
        return resources
