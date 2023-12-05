from dnotes.db.example_db import users


def check_user_login_data(username, password):
    """
    check user's login details

    """
    for user in users.values():
        if user["user_name"] == username and user["password"] == password:
            print(user)
            return True
    return False






