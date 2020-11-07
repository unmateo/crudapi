from fastapi.testclient import TestClient
from pytest import fixture

from crudapi.api import CrudAPI
from crudapi.models.base import BaseModel
from crudapi.services.database import engine


@fixture(scope="session")
def renew_db():
    BaseModel.metadata.drop_all(engine)
    BaseModel.metadata.create_all(engine)


@fixture
def app(renew_db):
    return CrudAPI(prefix="/books")


@fixture
def client(app):
    return TestClient(app)
