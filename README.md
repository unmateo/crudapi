# CrudAPI: The easiest way to create your CRUD APIs

Combining the power of FastAPI, Pydantic and SQLAlchemy, you'll only have to care about modeling your data and we'll take care of building up a RESTful API for it.

```python
from crudapi import CrudAPI
from crudapi.models.api import BaseAPI
from crudapi.models.orm import BaseORM

from sqlalchemy import Column
from sqlalchemy import String


class BookORM(BaseORM):

    __tablename__ = "books"
    title = Column(String, nullable=False)


crud = CrudAPI(orm_model=BookORM)

```

you'll get, out of the box, a working _crudapi_ with all these working REST endpoints:

- GET: /books
- POST: /books
- GET: /books/\<id>
- PUT: /books/\<id>
- PATCH: /books/\<id>
- DELETE: /books/\<id>

and because CrudAPI subclasses FastAPI you'll also get all the incredible features of this wonderful library.

---

## Development

We use Poetry for packaging and dependency management:

`poetry install`

`poetry shell`

We use Pytest for testing:

`pytest`

You can start a testing server running:

`uvicorn tests.server:app --reload `
