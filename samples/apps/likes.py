from crudapi import CrudAPI
from samples.db import renew_db
from samples.models import Like
from samples.models import LikeCreate
from samples.models import Tag


def Likes():
    app = CrudAPI()
    app.include_model(orm_model=Like, create_model=LikeCreate)
    app.include_model(orm_model=Tag)
    renew_db()
    return app
