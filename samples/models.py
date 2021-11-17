from typing import List
from typing import Optional

from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel

from crudapi.models import BaseModel


class TestModel(BaseModel, table=True):
    field: str = Field()


class BookUpdate(SQLModel, table=False):

    description: Optional[str] = Field(nullable=True)
    review: Optional[str] = Field(nullable=True)


class BookWithTitle(BookUpdate):
    title: str = Field(nullable=False)


class BookWithoutAuthor(BookWithTitle, BaseModel):
    pass


class BookCreate(BookWithTitle):

    author_id: str = Field(foreign_key="authors.id")


class AuthorUpdate(SQLModel, table=False):

    name: Optional[str] = Field(nullable=True)


class AuthorCreate(AuthorUpdate):
    pass


class AuthorWithoutBooks(AuthorCreate, BaseModel):
    pass


class BookResponse(BookCreate, BaseModel):

    author: Optional[AuthorWithoutBooks] = None


class AuthorResponse(AuthorCreate, BaseModel):
    books: List[BookWithoutAuthor] = []


class Author(AuthorCreate, BaseModel, table=True):

    __tablename__ = "authors"

    books: List["Book"] = Relationship(back_populates="author")


class Book(BookCreate, BaseModel, table=True):

    __tablename__ = "books"
    author: Optional[Author] = Relationship(back_populates="books")


def include_authors(app):
    app.include_model(
        orm_model=Author,
        response_model=AuthorResponse,
        create_model=AuthorCreate,
        update_model=AuthorUpdate,
    )


def include_books(app):
    app.include_model(
        orm_model=Book,
        response_model=BookResponse,
        create_model=BookCreate,
        update_model=BookUpdate,
    )
