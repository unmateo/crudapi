from sqlmodel import Field

from crudapi.api import CrudAPI
from crudapi.core.database import engine
from crudapi.models.orm import BaseORM


class Book(BaseORM, table=True):

    __tablename__ = "books"

    title: str = Field(nullable=False)


def migrate_db():
    Book.metadata.drop_all(engine)
    Book.metadata.create_all(engine)


def create_app():
    migrate_db()
    return CrudAPI(
        orm_model=Book,
        response_model=Book,
        create_model=Book,
        update_model=Book,
        title="Books",
    )
