from uuid import uuid4

from fastapi.testclient import TestClient
from pytest import fixture

from crudapi.api import CrudAPI
from tests.helpers import include_authors
from tests.helpers import include_books
from tests.helpers import multiapp


@fixture
def authors_app():
    app = CrudAPI()
    include_authors(app)
    return app


@fixture
def books_app():
    app = CrudAPI()
    include_books(app)
    return app


@fixture
def app():
    return multiapp()


@fixture
def client(app):
    return TestClient(app)


@fixture
def uuid():
    return uuid4()
