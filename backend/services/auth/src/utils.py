from model import User, RegisterRequest

def get_user_by_email(db, email: str) -> User:
    return {"user_id": "1", "email": email, "password": "123", "username": "ollie"}

def get_user_by_usernamel(db, username: str) -> User:
    return {"user_id": "1", "email": "email@gmail.com", "password": "123", "username": username}

def valid_user_register(db, u: RegisterRequest) -> bool:
    """ Check for username and/or email taken
    """
    return True

def create_user(db, u) -> User:
    """ Create user in db
    """
    return