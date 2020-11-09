from contextlib import contextmanager

from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

from crudapi.core.config import settings
from crudapi.core.logging import logger


engine = engine_from_config(settings.DB.dict(exclude_none=True), prefix="")


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
    except Exception as e:
        session.rollback()
        logger.exception(e)
        raise
    finally:
        session.close()


def alive():
    """ """
    try:
        with get_session() as session:
            session.execute("SELECT 1")
        return True
    except:
        return False


def check_connection():
    """ """
    if alive():
        logger.info("database connected")
    else:
        logger.warn("database not connected")
