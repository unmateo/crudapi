from logging import Formatter
from logging import getLogger
from logging import StreamHandler
from sys import stdout

from crudapi.core.config import settings


def get_logger(name="crudapi"):
    logger = getLogger(name)
    logger.setLevel(settings.LOG_LEVEL)
    log_handler = StreamHandler(stdout)
    formatter = Formatter(
        fmt="%(asctime)s - %(levelname)s - %(module)s.py:%(lineno)d:%(funcName)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S%z",
    )
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    return logger


logger = get_logger()
