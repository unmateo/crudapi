from fastapi import HTTPException

from crudapi.core.logging import logger


class HandledException(HTTPException):

    message = "Ups! There was an error"
    status_code = 500

    def __init__(self, detail=""):
        super().__init__(status_code=self.status_code, detail=self.message)
        logger.exception(f"{self}: {detail}")

    def __str__(self):
        return self.__class__.__name__


class NotFound(HandledException):
    message = "Resource not found"
    status_code = 404


class AlreadyExists(HandledException):
    message = "Resource already exists"
    status_code = 409


class ServiceUnavailable(HandledException):
    message = "Try again later"
    status_code = 503


class InvalidCredentials(HandledException):

    message = "Invalid credentials"
    status_code = 401


class InvalidParameters(HandledException):
    message = "Invalid parameters"
    status_code = 422
