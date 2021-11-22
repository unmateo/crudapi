from json import dump
from json import load

from crudapi import CrudAPI


OPENAPI = "tests/core/openapi.json"


def test_defaults(SimpleModel):

    app = CrudAPI()
    app.include_model(SimpleModel)


def test_multiapp_openapi(client):
    openapi = client.get("/openapi.json").json()
    with open(OPENAPI) as file:
        expected = load(file)
    assert openapi == expected


def dump_openapi(openapi):
    with open(OPENAPI, "w") as file:
        dump(openapi, file)
