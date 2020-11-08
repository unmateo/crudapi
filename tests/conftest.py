from fastapi.testclient import TestClient
from pytest import fixture

from tests.helpers import create_app
from tests.helpers import migrate_db


@fixture(scope="session")
def renew_db():
    migrate_db()


@fixture
def app(renew_db):
    return create_app()


@fixture
def client(app):
    return TestClient(app)
