from typing import Union
from fastapi import FastAPI, Request, Depends, Response, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from redis.asyncio import Redis
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from pydantic import BaseModel
from schemas import LoginRequest, RegisterRequest
import httpx
import jwt
import os


JWT_SECRET = os.getenv("JWT_SECRET")
AUTH_URL = os.getenv("AUTH_SERVICE_URL")
PROMPT_URL = os.getenv("PROMPT_SERVICE_URL")
REDIS_URL = os.getenv("REDIS_SERVICE_URL")

app = FastAPI()
security = HTTPBearer()

@app.on_event("startup")
async def startup():
    redis = Redis.from_url(REDIS_URL, decode_responses=True)
    await FastAPILimiter.init(redis)

@app.post("/login")
async def proxy_login(req: LoginRequest, dependencies=[Depends(RateLimiter(times=5, seconds=60))]):
    """
    Handle login and return a JWT token.
    """
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{AUTH_URL}/login",  # Docker service name + port
            json=req.dict(),
            timeout=10.0
        )
    return Response(
        content=resp.content,
        status_code=resp.status_code,
        media_type=resp.headers.get("content-type", "application/json")
    )

@app.post("/register")
async def proxy_login(req: RegisterRequest, dependencies=[Depends(RateLimiter(times=5, seconds=60))]):
    """
    Handle login and return a JWT token.
    """
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{AUTH_URL}/register",  # Docker service name + port
            json=req.dict(),
            timeout=10.0
        )
    return Response(
        content=resp.content,
        status_code=resp.status_code,
        media_type=resp.headers.get("content-type", "application/json")
    )

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
    dependencies=[Depends(RateLimiter(times=3, seconds=60))]  # Rate limit this endpoint
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