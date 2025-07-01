from model import User
from schemas import RegisterRequest
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession as As
from sqlalchemy.future import select
from sqlalchemy import or_
from security import get_password_hash

async def get_user_by_email(db: As, email: str) -> Optional[User]:
    query = select(User).where(User.email == email)
    result = await db.execute(query)
    return result.scalars().first()

async def get_user_by_username(db: As, username: str) -> Optional[User]:
    query = select(User).where(User.username == username)
    result = await db.execute(query)
    return result.scalars().first()

async def valid_user_register(db, u: RegisterRequest) -> bool:
    """ Check for username and/or email taken
    """
    query = select(User).where(or_(User.email == u.email, User.username == u.username))
    result = await db.execute(query)
    user = result.scalars().first()
    return user is None

async def create_user(db, u) -> User:
    """ Create user in db
    """
    hashed_pw = get_password_hash(u.password)
    new_user = User(
        email=u.email,
        password=u.password,  # Ensure password is hashed in production
        username=u.username
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
