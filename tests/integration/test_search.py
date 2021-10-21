def test_search_all(client):

    response = client.get("/books").json()
    assert response == []


def test_search_one(client):

    model = {"title": "APIs for dummies", "author_id": "sarasa"}
    created = client.post("/books", json=model).json()
    id = created.get("id")
    searched = client.get(f"/books/{id}")
    assert searched.json() == created


def test_search_one_not_found_returns_404(client, uuid):

    response = client.get(f"/books/{uuid}")
    assert response.status_code == 404


def test_paginator(client):

    model_1 = {"title": "APIs for dummies", "author_id": "sarasa"}
    model_2 = {"title": "Great APIs for dummies", "author_id": "sarasa"}

    created_1 = client.post("/books", json=model_1).json()
    client.post("/books", json=model_2).json()

    searched = client.get(f"/books?limit=1&offset=1")

    assert searched.json() == [created_1]


def test_default_paginator(client):

    books = []
    for i in range(20):
        model = {"title": f"{i}", "author_id": "sarasa"}
        book = client.post("/books", json=model).json()
        books.append(book)

    searched = client.get(f"/books").json()

    assert len(searched) == 10
    assert searched[0]["title"] == "19"
    assert searched[-1]["title"] == "10"
