from crudapi import CrudAPI
from samples.db import renew_db
from samples.models import include_books


def Books():
    app = CrudAPI()
    include_books(app)
    renew_db()
    return app
