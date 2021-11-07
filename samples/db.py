from crudapi.core.database import engine
from crudapi.core.database import get_session
from crudapi.models import BaseModel


def renew_db():
    with get_session() as db:
        db.execute("PRAGMA foreign_keys=ON")
    BaseModel.metadata.drop_all(engine)
    BaseModel.metadata.create_all(engine)
