def test_patch(client):

    # creates
    model = {"title": "APIs for dummies"}
    created = client.post("/books", json=model).json()
    id = created.get("id")
    # patches
    fields = {"title": "APIs for experts"}
    patched = client.patch(f"/books/{id}", json=fields).json()
    assert patched.get("title") == fields.get("title")
    assert patched.get("updated") > created.get("updated")
    # asserts
    response = client.get(f"/books/{id}").json()
    assert response.get("title") == fields.get("title")


def test_patch_not_found_returns_404(client):

    response = client.patch("/books/sarasa", json={"title": "fake"})
    assert response.status_code == 404
