from db.dependency import get_db
from dnotes.db.example_db import users
from fastapi.encoders import jsonable_encoder
from dnotes.schemas.user import UserCreate


class UserCrud:

    def __init__(self, db):
        self.db = db

    def create(self, user: UserCreate):  # add new user
        new_id = max(users.keys()) + 1
        users[new_id] = {
            "id": new_id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "user_name": user.user_name,
            "email": user.email,
            "password": user.password
        }


    def get_by_id(self, note_id: int):
        pass

    def update(self):
        pass

    def delete(self):
        pass


def create_user_crud():
    db = get_db()
    crud = UserCrud(db=db)
    return crud


