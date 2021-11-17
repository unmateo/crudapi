from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import fixture

from crudapi.mixins import DeleteMixin


def test_delete_one(given_delete_mixin_app_client, db, TestModel):
    test_model = create_test_model(db, TestModel)
    client = given_delete_mixin_app_client
    response = client.delete(f"/testmodel/{test_model.id}").json()
    assert_response_is_expected_model(response, test_model)
    assert_model_was_deleted(db, test_model, TestModel)


def assert_response_is_expected_model(response, model):
    assert response["field"] == model.field
    assert response["id"] == model.id
    assert response["created_at"] == model.created_at.isoformat()
    assert response["updated_at"] == model.updated_at.isoformat()


def assert_model_was_deleted(db, test_model, TestModel):
    model_id = test_model.id
    db.expire(test_model)
    assert db.query(TestModel).get(model_id) is None


@fixture
def given_delete_mixin_app_client(TestModel):
    class TestAPI(FastAPI, DeleteMixin):
        pass

    app = TestAPI()
    app.delete_router(TestModel)
    client = TestClient(app)
    return client


def create_test_model(db, TestModel):
    model = TestModel(field="test")
    db.add(model)
    db.commit()
    return model
