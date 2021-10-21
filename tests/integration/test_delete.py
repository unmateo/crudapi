def test_delete(client):

    # creates
    model = {"title": "APIs for dummies", "author_id": "sarasa"}
    created = client.post("/books", json=model).json()
    id = created.get("id")
    # deletes
    deleted = client.delete(f"/books/{id}").json()
    assert deleted == created
    # asserts
    response = client.get(f"/books/{id}")
    assert response.status_code == 404


def test_delete_not_found_returns_404(client, uuid):

    response = client.delete(f"/books/{uuid}")
    assert response.status_code == 404
