# CrudAPI: The easiest way to create your CRUD APIs

[![codecov](https://codecov.io/gh/unmateo/crudapi/branch/develop/graph/badge.svg?token=RAKVPGHZU5)](https://codecov.io/gh/unmateo/crudapi)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI version](https://badge.fury.io/py/crudapi.svg)](https://badge.fury.io/py/crudapi)


Assuming you define your SQLAlchemy model BookORM in your module _books.models_, with this code snippet:

```python
from crudapi import CrudAPI

from books.models import BookORM


crud = CrudAPI(orm=BookORM, prefix="books")

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

You can start a testing server running:

`uvicorn tests.server:app --reload `
