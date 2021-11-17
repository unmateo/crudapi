from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import fixture

from crudapi.mixins.search import SearchMixin


def test_get_one(test_model, given_search_mixin_app_client):
    client = given_search_mixin_app_client
    response = client.get(f"/testmodel/{test_model.id}").json()
    assert_response_is_expected_model(response, test_model)


def test_get_all(test_model, given_search_mixin_app_client):

    client = given_search_mixin_app_client
    response = client.get(f"/testmodel").json()[0]
    assert_response_is_expected_model(response, test_model)


@fixture
def test_model(db, TestModel):
    model = TestModel(field="test")
    db.add(model)
    db.commit()
    return model


@fixture
def given_search_mixin_app_client(TestModel):
    class TestAPI(FastAPI, SearchMixin):
        pass

    app = TestAPI()
    app.search_router(TestModel)
    client = TestClient(app)
    return client


def assert_response_is_expected_model(response, model):
    assert response["field"] == model.field
    assert response["id"] == model.id
    assert response["created_at"] == model.created_at.isoformat()
    assert response["updated_at"] == model.updated_at.isoformat()
