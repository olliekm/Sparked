from fastapi import FastAPI, HTTPException
from model import LoginRequest, RegisterRequest
from utils import get_user_by_email, get_user_by_username, create_user
from security import verify_password, create_access_token

app = FastAPI()
db = 'MAKE DATABASE CONNECTION SEND AS REFERENCE'

@app.post('/login')
async def handle_login(u: LoginRequest):
    user = await get_user_by_email(u.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if verify_password(u.password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    token = create_access_token({"user_id": user.user_id})
    return {"access_token": token}

@app.post('/register')
async def handle_register(u: RegisterRequest):
    if await get_user_by_email(db, u.email):
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )
    if await get_user_by_username(db, u.username):
        raise HTTPException(
            status_code=409,
            detail="Username already taken"
        )
    user = create_user(db, u)
    # Don't send back token, require them to login with their credentials after

