from sqlalchemy import Column, String, Integer, ForeignKey
from db import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    username = Column(String, unique=True, index=True)

    def __repr__(self):
        return f"<User(user_id={self.user_id}, email={self.email}, username={self.username})>"