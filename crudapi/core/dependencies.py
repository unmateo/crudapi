from crudapi.core.database import get_session


def db():
    """Yields a db session."""
    with get_session() as session:
        yield session
