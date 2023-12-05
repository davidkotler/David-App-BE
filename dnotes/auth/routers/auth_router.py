from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter
from fastapi import HTTPException, status
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm

from dnotes.auth.services.handle_login import check_user_login_data
from dnotes.auth.token import create_access_token
from dnotes.db.Crud.UserCrud import create_user_crud
from dnotes.schemas.user import UserCreate, UserLogin

ACCESS_TOKEN_EXPIRE_MINUTES = 30
router = APIRouter()


@router.post("/", status_code=200)
def register(user: UserCreate):
    print(user.user_name)
    print(user.password)
    crud = create_user_crud()
    crud.create(user)


@router.post("/login", status_code=200)
def user_login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):  # add OAuth2PasswordRequestForm later
    if not (check_user_login_data(form_data.username, form_data.password)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    # username = form_data.username
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    print(access_token)
    return {"access_token": access_token, "token_type": "bearer"}
