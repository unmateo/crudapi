CrudAPI: The easiest way to create your CRUD APIs
=======

Assuming you define your models BookAPI and BookORM in your module _books.models_, with this code snippet:

```python
from crudapi import CrudAPI
from fastapi import FastAPI

from books.models import BookAPI
from books.models import BookORM


app = FastAPI()

crud = CrudAPI(api=BookAPI, orm=BookORM)

app.include_router(crud, prefix="/books", tags=["Book"])

```

you'll get, out of the box, a working _crudapi_ with all these working endpoints:

- GET: /books
- POST: /books
- GET: /books/:id:
- PUT: /books/:id:
- PATCH: /books/:id:
- DELETE: /books/:id:

---
## Persistance

We provide a default SQLite/SQLAlchemy persistance layer, but you can easily replace it with your own implementation.



---
## Development


We use Poetry for packaging and dependency management:

`poetry install`

`poetry shell`

We use Pytest for testing:

`pytest`

