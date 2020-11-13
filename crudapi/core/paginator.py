from pydantic import BaseModel

from crudapi.core.config import settings
from crudapi.core.types import QueryLimit
from crudapi.core.types import QueryOffset


class BasePaginator(BaseModel):

    limit: QueryLimit = settings.DEFAULT_LIMIT
    offset: QueryOffset = settings.DEFAULT_OFFSET
