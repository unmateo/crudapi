from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
now = datetime.utcnow


class BaseModel(Base):

    __abstract__ = True

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid4()),
        unique=True,
        nullable=False,
    )
    created = Column(DateTime(timezone=True), default=now)
    updated = Column(DateTime(timezone=True), default=now, onupdate=now)

    def __repr__(self) -> str:
        return str(self.id)

    @classmethod
    def name(cls):
        return cls.__name__
