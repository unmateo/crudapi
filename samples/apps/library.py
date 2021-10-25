from crudapi.api import CrudAPI
from samples.db import renew_db
from samples.models import include_authors
from samples.models import include_books


def Library():
    app = CrudAPI(title="Library")
    include_authors(app)
    include_books(app)
    renew_db()
    return app
