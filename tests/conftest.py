from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel
from pytest import fixture


@fixture
def app():
    return FastAPI()


@fixture
def client(app):
    return TestClient(app)


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