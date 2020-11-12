from pydantic import BaseModel
from sqlalchemy import Column
from sqlalchemy import String

from crudapi.api import CrudAPI
from crudapi.core.database import engine
from crudapi.models.api import BaseAPI
from crudapi.models.orm import BaseORM


class BookORM(BaseORM):

    __tablename__ = "books"
    title = Column(String, nullable=False)


class BookCreate(BaseModel):
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
        orm_model=BookORM,
        response_model=Book,
        create_model=BookCreate,
        update_model=BookUpdate,
        title="Books",
    )
