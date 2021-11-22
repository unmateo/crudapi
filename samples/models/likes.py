from typing import List

from pydantic import validator
from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel

from crudapi import BaseModel


class TagLike(BaseModel, table=True):

    __tablename__ = "tags_likes"

    tag_id: str = Field(primary_key=True, foreign_key="tags.id")
    like_id: str = Field(primary_key=True, foreign_key="likes.id")


class Tag(BaseModel, table=True):
    __tablename__ = "tags"
    tag: str = Field(index=True, nullable=False)

    @validator("tag")
    def to_uppercase(cls, value: str):
        return value.upper()


class LikeCreate(SQLModel):
    url: str = Field(nullable=False)
    title: str = Field(nullable=False)
    tags: List[str] = []


class Like(BaseModel, LikeCreate, table=True):
    __tablename__ = "likes"
    tags: List[Tag] = Relationship(link_model=TagLike)
