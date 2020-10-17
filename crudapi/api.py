from fastapi.routing import APIRouter

from crudapi.routers.read import ReadRouter
from crudapi.services.read import ReadService

class CrudAPI(APIRouter):

    def __init__(
        self,
        request,
        response,
        read_router=ReadRouter,
        read_service=ReadService,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        read = read_router(service=read_service(), request=request, response=response)
        self.include_router(read)
