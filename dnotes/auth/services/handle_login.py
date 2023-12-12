from dnotes.db.example_db import users
from dnotes.db.Models.user_model import User


def check_user_login_data(username, password, db):
    """
    check user's login details

    """

    user = db.query(User).filter(User.user_name == username, User.password == password).first()

    # If a user is found, return True, otherwise return False
    return user is not None







