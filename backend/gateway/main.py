from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import jwt
import prompt

app = FastAPI()

class PromptRequest(BaseModel):
    journal: str


class LoginRequest(BaseModel):
    email: str
    password: str

@app.post("/prompt")
def read_root(req: PromptRequest):
    result = prompt.get_prompt_response(req.journal)
    return result

@app.post("/login")
def handle_login(req: LoginRequest):
    """
    Handle login and return a JWT token.
    """
    # In a real application, you would validate the user credentials here
    payload = {"user": req.login, "email": req.email}

    token = jwt.encode(payload, "secret", algorithm="HS256")
    return {"token": token}