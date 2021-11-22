from crudapi import CrudAPI
from samples.db import renew_db
from samples.models import SimpleModel


def SimpleAPI():
    app = CrudAPI()
    app.include_model(orm_model=SimpleModel)
    renew_db()
    return app
