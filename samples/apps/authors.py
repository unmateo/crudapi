from crudapi.api import CrudAPI
from samples.db import renew_db
from samples.models import include_authors


def Authors():
    app = CrudAPI()
    include_authors(app)
    renew_db()
    return app
