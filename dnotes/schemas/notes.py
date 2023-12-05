"""schemas for notes """

from pydantic import BaseModel
from typing import Optional


class NoteBase(BaseModel):
    id: int
    title: str
    content: str


class NoteCreate(BaseModel):
    title: str
    content: str


class NoteGet(BaseModel):
    id: int
    title: str
    content: str


class NoteUpdate(BaseModel):

    title: Optional[str]
    content: Optional[str]
