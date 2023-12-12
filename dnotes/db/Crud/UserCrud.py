from db.dependency import get_db, Session
from fastapi.encoders import jsonable_encoder
from dnotes.schemas.user import UserCreate , UserUpdate
from dnotes.db.Models.user_model import User


class UserCrud:

    def __init__(self, db):
        self.db = db

    def create(self, user: UserCreate):
        # Convert UserCreate to dict and create a new User instance
        user_dict = jsonable_encoder(user)
        db_user = User(**user_dict)

        # Add the user to the database and commit the transaction
        self.db.add(db_user)
        self.db.commit()

        # Refresh the user instance to get the updated values from the database
        self.db.refresh(db_user)

        return db_user

    def get_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def update(self, user_id: int, user_update: UserUpdate):

        db_user = self.get_by_id(user_id)
        if db_user:

            update_data = jsonable_encoder(user_update)
            for field in update_data:
                setattr(db_user, field, update_data[field])

            self.db.commit()
            self.db.refresh(db_user)

        return db_user


    def delete(self, user_id: int):
        db_user = self.get_by_id(user_id)

        if db_user:
            self.delete(db_user)


def create_user_crud():
    db: Session = get_db()
    db = next(db) # try this
    crud = UserCrud(db=db)
    return crud


