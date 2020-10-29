from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel
from pytest import fixture

from crudapi.api import CrudAPI


@fixture
def BookRequest():

    class BookRequest(BaseModel):
        title: str
    
    return BookRequest


@fixture
def BookResponse(BookRequest):

    class BookResponse(BookRequest):
        id: str
    
    return BookResponse


@fixture
def app(BookRequest, BookResponse):
    app = FastAPI()
    crud = CrudAPI(request=BookRequest, response=BookResponse)
    app.include_router(crud, prefix="/books")
    return app

@fixture
def client(app):
    return TestClient(app)
