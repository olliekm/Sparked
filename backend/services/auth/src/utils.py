from model import User, RegisterRequest

def get_user_by_email(email: str) -> User:
    return {"user_id": "1", "email": email, "password": "123", "username": "ollie"}

def get_user_by_usernamel(username: str) -> User:
    return {"user_id": "1", "email": "email@gmail.com", "password": "123", "username": username}

def valid_user_register(u: RegisterRequest) -> bool:
    """ Check for username and/or email taken
    """
    return True