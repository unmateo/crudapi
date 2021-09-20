def test_patch(client):

    # creates
    model = {"description": "APIs for dummies", "title": "Magic APIs"}
    created = client.post("/books", json=model).json()
    id = created.get("id")
    # patches
    fields = {"description": "APIs for experts"}
    patched = client.patch(f"/books/{id}", json=fields).json()
    assert patched.get("description") == fields.get("description")
    assert patched.get("updated_at") > created.get("updated_at")
    # asserts
    response = client.get(f"/books/{id}").json()
    assert response.get("description") == fields.get("description")


def test_patch_not_found_returns_404(client, uuid):

    response = client.patch(f"/books/{uuid}", json={"title": "fake"})
    assert response.status_code == 404
