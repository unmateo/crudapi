from crudapi.api import CrudAPI


def test_read(app, client, BookRequest, BookResponse):

    crud = CrudAPI(request=BookRequest, response=BookResponse)

    app.include_router(crud, prefix="/users")

    get_all = client.get("/users").json()
    assert get_all == []

    import pdb; pdb.set_trace() # DEBUG

    get_one = client.get("/users/sarasa").json()
    assert get_one == {'id': 'sarasa', 'title': 'titulo'}

