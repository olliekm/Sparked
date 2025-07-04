from pydantic import BaseModel, EmailStr, Field

class LoginRequest(BaseModel):
    email: EmailStr = Field(..., examples="you@example.com")
    password: str = Field(..., min_length=8, examples="123jkb!dklqw")

class RegisterRequest(BaseModel):
    email: EmailStr = Field(..., examples="you@example.com")
    password: str = Field(..., min_length=8, examples="123jkb!dklqw")
    username: str = Field(..., max_length=10, examples="oliverkm")

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class User(BaseModel):
    user_id: str = Field(..., examples="21312312289")
    email: str = Field(..., examples="you@example.com")
    password: str = Field(..., examples="fy2gewouycwekuachb")
    username: str = Field(..., examples="user123")

class PromptRequest(BaseModel):
    journal: str

class LoginRequest(BaseModel):
    email: str
    password: str