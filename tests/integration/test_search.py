

def test_search_all(client):

    response = client.get("/books").json()
    assert response == [{'id': 'sarasa', 'title': 'titulo'}]


def test_search_one(client):

    response = client.get("/books/sarasa")
    assert response.json() == {'id': 'sarasa', 'title': 'titulo'}


def test_search_one_not_found_returns_404(client):

    response = client.get("/books/sarasa")
    assert response.status_code == 404
