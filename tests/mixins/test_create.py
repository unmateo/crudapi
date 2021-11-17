from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import fixture

from crudapi.mixins import CreateMixin


def test_create_one(given_create_mixin_app_client):
    test_model = {"field": "field"}
    client = given_create_mixin_app_client
    response = client.post(f"/testmodel", json=test_model).json()
    assert_response_is_expected_model(response, test_model)


@fixture
def given_create_mixin_app_client(TestModel):
    class TestAPI(FastAPI, CreateMixin):
        pass

    app = TestAPI()
    app.create_router(TestModel)
    client = TestClient(app)
    return client


def assert_response_is_expected_model(response, model):
    assert response["field"] == model["field"]
    assert response["id"]
    assert response["created_at"]
    assert response["updated_at"]
