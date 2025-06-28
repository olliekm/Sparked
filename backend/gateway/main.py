from typing import Union
from fastapi import FastAPI, Request, Depends, Response, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import httpx
import jwt
import os

JWT_SECRET = os.getenv("JWT_SECRET")
app = FastAPI()
security = HTTPBearer()

class PromptRequest(BaseModel):
    journal: str


class LoginRequest(BaseModel):
    email: str
    password: str

@app.post("/login")
def handle_login(req: LoginRequest):
    """
    Handle login and return a JWT token.
    """
    # In a real application, you would validate the user credentials here
    payload = {"user": req.login, "email": req.email}

    token = jwt.encode(payload, "secret", algorithm="HS256")
    return {"token": token}

def verify_jwt(creds: HTTPAuthorizationCredentials = Depends(security)):

    token = creds.credentials
    try:
        # decode & verify signature + expiry
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(401, "Token expired")
    except jwt.PyJWTError:
        raise HTTPException(401, "Invalid token")
    # return full payload so downstream can grab user_id, roles, etc.
    return payload

@app.post("/prompt")
async def proxy_prompt(
    request: Request,
    token_payload: dict = Depends(verify_jwt),
):
    body = await request.json()
    user_id = token_payload.get("user_id")
    if not user_id:
        raise HTTPException(401, "Invalid token payload")

    # forward to prompting service
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "http://prompt-service:8001/prompt",  # Docker service name + port
            json=body,
            headers={"X-User-ID": str(user_id)},
            timeout=10.0
        )

    # pass back whatever the prompting service returned
    return Response(
        content=resp.content,
        status_code=resp.status_code,
        media_type=resp.headers.get("content-type", "application/json")
    )