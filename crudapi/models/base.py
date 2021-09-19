from datetime import datetime
from typing import Optional
from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlmodel import Field
from sqlmodel import SQLModel


def uuid():
    return str(uuid4())


now = datetime.utcnow


class BaseModel(SQLModel, table=False):

    id: str = Field(default_factory=uuid, primary_key=True)
    created_at: Optional[datetime] = Field(
        sa_column=Column(DateTime, default=now, nullable=False)
    )
    updated_at: Optional[datetime] = Field(
        sa_column=Column(DateTime, default=now, onupdate=now)
    )
