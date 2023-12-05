from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):

    id: int
    first_name: str
    last_name: str
    user_name: str
    email: str
    password: str


class UserCreate(BaseModel):

    first_name: str
    last_name: str
    user_name: str
    email: str
    password: str


class UserLogin(BaseModel):

    user_name: str
    password: str


class UserUpdate(UserBase):

    first_name: str
    last_name: str
    user_name: str
    email: str
    password: str


class UserDelete(UserBase):

    id: int

