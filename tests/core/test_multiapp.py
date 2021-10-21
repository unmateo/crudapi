from json import load


def test_multiapp_openapi(client):
    openapi = client.get("/openapi.json").json()
    with open("tests/core/openapi.json") as file:
        expected = load(file)
    assert openapi == expected
