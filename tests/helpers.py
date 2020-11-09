from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Column
from sqlalchemy import String

from crudapi.api import CrudAPI
from crudapi.core.base_model import BaseORM
from crudapi.core.database import engine


class BookORM(BaseORM):

    __tablename__ = "books"
    title = Column(String, nullable=False)


class BookBase(BaseModel):
    class Config:

        orm_mode = True


class BaseAPI(BookBase):
    id: str
    created: datetime
    updated: datetime


class BookCreate(BookBase):
    title: str


class BookUpdate(BookCreate):
    pass


class Book(BookCreate, BaseAPI):
    pass


def migrate_db():
    BookORM.metadata.drop_all(engine)
    BookORM.metadata.create_all(engine)


def create_app():
    migrate_db()
    return CrudAPI(
        prefix="/books",
        orm_model=BookORM,
        response_model=Book,
        create_model=BookCreate,
        update_model=BookUpdate,
        title="Books",
    )
