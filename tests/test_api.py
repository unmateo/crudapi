

def test_read_all(client):

    get_all = client.get("/books").json()
    assert get_all == []

def test_read_one(client):

    get_one = client.get("/books/sarasa").json()
    assert get_one == {'id': 'sarasa', 'title': 'titulo'}
