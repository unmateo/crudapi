from crudapi import CrudAPI


def test_defaults(TestModel):

    app = CrudAPI()
    app.include_model(TestModel)
