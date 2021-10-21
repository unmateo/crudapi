from typing import List
from typing import Optional

from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel

from crudapi.api import CrudAPI
from crudapi.core.database import engine
from crudapi.core.database import get_session
from crudapi.models.base import BaseModel


class AuthorUpdate(SQLModel, table=False):

    name: Optional[str] = Field(nullable=True)


class AuthorCreate(AuthorUpdate):
    pass


class Author(AuthorCreate, BaseModel, table=True):

    __tablename__ = "authors"

    books: List["Book"] = Relationship(back_populates="author")


class BookUpdate(SQLModel, table=False):

    description: Optional[str] = Field(nullable=True)
    review: Optional[str] = Field(nullable=True)


class BookCreate(BookUpdate):

    title: str = Field(nullable=False)
    author_id: str = Field(foreign_key="authors.id")


class Book(BookCreate, BaseModel, table=True):

    __tablename__ = "books"
    author: Optional[Author] = Relationship(back_populates="books")


def include_authors(app):
    app.include_model(
        orm_model=Author, create_model=AuthorCreate, update_model=AuthorUpdate
    )


def include_books(app):
    app.include_model(
        orm_model=Book,
        create_model=BookCreate,
        update_model=BookUpdate,
    )


def renew_db():
    with get_session() as db:
        db.execute("PRAGMA foreign_keys=ON")
    BaseModel.metadata.drop_all(engine)
    BaseModel.metadata.create_all(engine)


def multiapp():
    app = CrudAPI(title="Library")
    include_authors(app)
    include_books(app)
    renew_db()
    return app
