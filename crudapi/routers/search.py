from fastapi.routing import APIRouter


search = APIRouter()


@search.get("/")
def get_all():
    """ """
    return [{'id': 'sarasa', 'title': 'titulo'}]

@search.get("/{id}")
def get_all(id):
    """ """
    return {'id': 'sarasa', 'title': 'titulo'}
