def test_delete(client):

    # creates
    model = {"title": "APIs for dummies"}
    created = client.post("/books", json=model).json()
    id = created.get("id")
    # deletes
    deleted = client.delete(f"/books/{id}").json()
    assert deleted == created
    # asserts
    response = client.get(f"/books/{id}")
    assert response.status_code == 404


def test_delete_not_found_returns_404(client):

    response = client.delete("/books/sarasa")
    assert response.status_code == 404
