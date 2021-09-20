from typing import Optional

from sqlmodel import Field
from sqlmodel import SQLModel

from crudapi.api import CrudAPI
from crudapi.core.database import engine
from crudapi.models.base import BaseModel


class BookUpdate(SQLModel, table=False):

    description: Optional[str] = Field(nullable=True)
    review: Optional[str] = Field(nullable=True)


class BookCreate(BookUpdate):

    title: str = Field(nullable=False)


class Book(BookCreate, BaseModel, table=True):

    __tablename__ = "books"


def migrate_db():
    Book.metadata.drop_all(engine)
    Book.metadata.create_all(engine)


def create_app():
    migrate_db()
    return CrudAPI(
        orm_model=Book,
        response_model=Book,  # Retrieve all fields
        create_model=BookCreate,
        update_model=BookUpdate,
        title="Books",
    )
