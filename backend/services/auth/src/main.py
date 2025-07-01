from fastapi import FastAPI, HTTPException, Depends
from model import LoginRequest, RegisterRequest
from sqlalchemy.ext.asyncio import AsyncSession as As
from utils import get_user_by_email, get_user_by_username, create_user
from security import verify_password, create_access_token
from db import get_db

app = FastAPI()

@app.post('/login')
async def handle_login(u: LoginRequest, db: As = Depends(get_db)):
    user = await get_user_by_email(u.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if verify_password(u.password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    token = create_access_token({"user_id": user.user_id})
    return {"access_token": token}

@app.post('/register')
async def handle_register(u: RegisterRequest, db: As = Depends(get_db)):
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
    new_user = create_user(db, u)
    return {"user_id": new_user.user_id, "email": new_user.email, "username": new_user.username}
    # Don't send back token, require them to login with their credentials after

