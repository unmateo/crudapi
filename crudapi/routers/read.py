from typing import List
from typing import Type

from pydantic import BaseModel
from fastapi.routing import APIRouter

class ReadRouter(APIRouter):

    def __init__(self, service, request, response: Type[BaseModel], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = service
        self.add_api_route("/", self.get_all, response_model=List[response])
        self.add_api_route("/{id}", self.get_one, response_model=response)


    def get_all(self):
        return self.service.get_all()

    
    def get_one(self, id):
        return self.service.get_one(id)
