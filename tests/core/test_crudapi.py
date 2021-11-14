from sqlmodel import Field

from crudapi import BaseModel
from crudapi import CrudAPI


def test_defaults():
    class TestModel(BaseModel, table=True):

        field: str = Field(default="test")

    app = CrudAPI()
    app.include_model(TestModel)
