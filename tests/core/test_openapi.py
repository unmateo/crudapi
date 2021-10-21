from crudapi.core.openapi import combine


def test_combine(authors_app, books_app):
    authors = authors_app.openapi()
    books = books_app.openapi()

    openapi = combine(authors, [books])

    assert openapi["openapi"] == authors["openapi"]
    assert openapi["info"] == authors["info"]

    paths = openapi["paths"]

    authors_paths = authors["paths"]
    books_paths = books["paths"]

    assert all([path in paths for path in authors_paths])
    assert all([path in paths for path in books_paths])

    schemas = openapi["components"]["schemas"]

    authors_schemas = authors["components"]["schemas"]
    books_schemas = books["components"]["schemas"]

    assert all([schema in schemas for schema in authors_schemas])
    assert all([schema in schemas for schema in books_schemas])
