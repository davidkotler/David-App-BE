from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter
from fastapi import HTTPException, status
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm

from dnotes.auth.services.handle_login import check_user_login_data
from dnotes.auth.token import create_access_token
from dnotes.db.Crud.UserCrud import create_user_crud
from dnotes.schemas.user import UserCreate, UserLogin, UserUpdate
from dnotes.db.dependency import Session, get_db




ACCESS_TOKEN_EXPIRE_MINUTES = 30
router = APIRouter()


@router.post("/", status_code=200)
def register(user: UserCreate):
    print(user.user_name)
    print(user.password)
    crud = create_user_crud()
    crud.create(user)


@router.post("/login", status_code=200)
def user_login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    if not (check_user_login_data(form_data.username, form_data.password, db)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    # username = form_data.username
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    print(access_token)
    return {"access_token": access_token, "token_type": "bearer"}


# @router.put("/update_user/{user_id}", status_code=200)
# def update_user(user_id, user: UserUpdate, current_user: str = Depends(get_current_user)):
#
#     if current_user != user_id:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="you dont have premission")
#
#     crud = create_user_crud()
#     updated = crud.update(user_id, user)
#
#     if not updated:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="failed to update user")

