def test_search_all(client):

    response = client.get("/books").json()
    assert response == []


def test_search_one(client):

    model = {"title": "APIs for dummies"}
    created = client.post("/books", json=model).json()
    id = created.get("id")
    searched = client.get(f"/books/{id}")
    assert searched.json() == created


def test_search_one_not_found_returns_404(client):

    response = client.get("/books/sarasa")
    assert response.status_code == 404
