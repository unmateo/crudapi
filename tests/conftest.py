from fastapi.applications import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel
from pytest import fixture

from crudapi.api import CrudAPI
from crudapi.config import Config


@fixture
def BookRequest():
    class BookRequest(BaseModel):
        title: str

    return BookRequest


@fixture
def BookResponse(BookRequest):
    class BookResponse(BookRequest):
        id: str

    return BookResponse


@fixture
def test_config():
    return Config()


@fixture
def app(test_config):
    return CrudAPI(prefix="/books", config=test_config)


@fixture
def client(app):
    return TestClient(app)
