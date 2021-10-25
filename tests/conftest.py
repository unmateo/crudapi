from uuid import uuid4

from fastapi.testclient import TestClient
from pytest import fixture

from samples.apps.authors import Authors
from samples.apps.books import Books
from samples.apps.library import Library


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
