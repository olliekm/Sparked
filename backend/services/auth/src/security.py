import jwt
import os
from datetime import datetime, timedelta
from passlib.hash import bcrypt

key = os.getenv("JWT_SECRET")
if not key:
    raise RuntimeError("Missing JWT_SECRET")

def create_access_token(user_id: str, expires_delta: timedelta = None) -> str:
    """ Create JWT with expiry delta
    """
    if expires_delta is None:
        expires_delta = timedelta(hours=24)
    payload = {
        "sub": user_id,
        "iat": datetime.now(),
        "exp": datetime.now() + expires_delta
    }
    return jwt.encode({"userId": user_id}, key, algorithm="HS256")

def verify_password(password: str, hashed_password: str) -> bool:
    """ Return true if password is correct
    """
    return bcrypt.verify(password, hashed_password)

def get_password_hash(password: str) -> str:
    """ Hash the password using bcrypt
    """
    return bcrypt.hash(password)