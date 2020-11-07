from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crudapi.core.config import settings


engine = create_engine(settings.DB_DSN)


@contextmanager
def get_session():
    """
    Yields a DB session on given datasource.
    On exception, rollbacks session.
    On success, commits and closes session.
    """
    maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = maker()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
