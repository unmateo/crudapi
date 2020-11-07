from sqlalchemy import Column
from sqlalchemy import String

from crudapi.models.base import BaseModel


class DefaultModel(BaseModel):

    __tablename__ = "books"

    title = Column(String, nullable=False)
