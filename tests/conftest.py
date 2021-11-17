from uuid import uuid4

from fastapi.testclient import TestClient
from pytest import fixture

from crudapi import BaseModel
from crudapi.core.database import engine
from crudapi.core.database import get_session
from samples.apps.authors import Authors
from samples.apps.books import Books
from samples.apps.library import Library
from samples.models import TestModel as _TestModel


@fixture
def TestModel():
    return _TestModel


@fixture
def authors_app():
    return Authors()


@fixture
def books_app():
    return Books()


@fixture
def app():
    return Library()


@fixture
def client(app):
    return TestClient(app)


@fixture
def uuid():
    return uuid4()


@fixture
def renew_db():
    BaseModel.metadata.drop_all(engine)
    BaseModel.metadata.create_all(engine)


@fixture
def db(renew_db):
    with get_session() as session:
        yield session
