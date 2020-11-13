from pydantic import conint

QueryLimit = conint(ge=0)
QueryOffset = conint(ge=0)
