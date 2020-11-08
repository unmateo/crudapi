from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from sqlalchemy import Column
from sqlalchemy import String

from crudapi.api import CrudAPI
from crudapi.core.base_model import BaseModel
from crudapi.services.database import engine


class ModelORM(BaseModel):

    __tablename__ = "books"
    title = Column(String, nullable=False)


ModelAPI = sqlalchemy_to_pydantic(ModelORM)


def migrate_db():
    ModelORM.metadata.drop_all(engine)
    ModelORM.metadata.create_all(engine)


def create_app():
    migrate_db()
    return CrudAPI(
        prefix="/books", orm_model=ModelORM, api_model=ModelAPI, title="Books"
    )
