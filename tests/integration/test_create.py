def test_create_ok(client):

    model = {"title": "APIs for dummies", "author_id": "sarasa"}
    response = client.post("/books", json=model).json()
    assert response.get("title") == model.get("title")
    assert response.get("created_at") is not None
    assert response.get("updated_at") is not None
