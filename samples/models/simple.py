from sqlmodel import Field

from crudapi.models import BaseModel


class SimpleModel(BaseModel, table=True):
    field: str = Field()
