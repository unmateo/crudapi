def test_patch(client):

    # creates
    model = {
        "description": "APIs for dummies",
        "title": "Magic APIs",
        "author_id": "sarasa",
    }
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

    response = client.patch(
        f"/books/{uuid}", json={"title": "fake", "author_id": "sarasa"}
    )
    assert response.status_code == 404


def test_put(client):

    # creates
    model = {
        "description": "APIs for dummies",
        "title": "Magic APIs",
        "author_id": "sarasa",
    }
    created = client.post("/books", json=model).json()
    id = created.get("id")
    # puts
    fields = {"title": "APIs for experts", "author_id": "sarasa"}
    patched = client.put(f"/books/{id}", json=fields).json()
    assert patched == 1
    # asserts
    response = client.get(f"/books/{id}").json()
    assert response.get("updated_at") > created.get("updated_at")
    assert response.get("title") == fields.get("title")
    assert response.get("description") is None
    assert response.get("review") is None


def test_put_not_found_returns_404(client, uuid):

    response = client.put(
        f"/books/{uuid}", json={"title": "fake", "author_id": "sarasa"}
    )
    assert response.status_code == 404
