from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import fixture

from crudapi import UpdateMixin


def test_update_one(test_model, given_update_mixin_app_client):
    update_model = {"field": "new_field"}
    client = given_update_mixin_app_client
    response = client.patch(f"/simplemodel/{test_model.id}", json=update_model).json()
    assert response["field"] == update_model["field"]
    assert response["id"] == test_model.id
    assert response["created_at"] == test_model.created_at.isoformat()
    assert response["updated_at"] > test_model.updated_at.isoformat()


def test_replace_one(test_model, given_update_mixin_app_client):
    update_model = {"field": "new_field"}
    client = given_update_mixin_app_client
    response = client.put(f"/simplemodel/{test_model.id}", json=update_model).json()
    assert response["field"] == update_model["field"]
    assert response["id"] == test_model.id
    assert response["created_at"] == test_model.created_at.isoformat()
    assert response["updated_at"] > test_model.updated_at.isoformat()


@fixture
def test_model(db, SimpleModel):
    model = SimpleModel(field="test")
    db.add(model)
    db.commit()
    return model


@fixture
def given_update_mixin_app_client(SimpleModel):
    class TestAPI(FastAPI, UpdateMixin):
        pass

    app = TestAPI()
    app.update_router(SimpleModel)
    client = TestClient(app)
    return client
