from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from crudapi.config import settings


engine = create_engine(settings.DB_DSN)


@contextmanager
def get_session():
    """
    Yields a DB session on given datasource.
    On exception, rollbacks session.
    On success, commits and closes session.
    """
    try:
        maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        session = maker()
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def is_alive(db: Session) -> bool:
    """ Returns a boolean indicating if given session is usable """

    try:
        db.execute("SELECT 1")
        return True
    except:
        return False
