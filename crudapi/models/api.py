from datetime import datetime

from pydantic import BaseModel


class BaseAPI(BaseModel):
    class Config:
        orm_mode = True

    id: str
    created: datetime
    updated: datetime
