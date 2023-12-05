import jwt
from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import PyJWTError
from typing import Annotated



# Secret key used to sign the token
SECRET_KEY = "your-secret-key"
# Token expiration time in minutes
ACCESS_TOKEN_EXPIRE_MINUTES = 30

ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    return user id depends on his token

    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = payload.get("sub")  # it return user name not user id, change later
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return user
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    # except Exception as e:
    #     raise e


