from typing import Union
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Depends, Response, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from redis.asyncio import Redis
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from prometheus_fastapi_instrumentator import Instrumentator
from pydantic import BaseModel
from schemas import LoginRequest, RegisterRequest
from prometheus_client import Counter, Histogram, make_asgi_app, CollectorRegistry, multiprocess
import httpx
import jwt
import os
import time


JWT_SECRET = os.getenv("JWT_SECRET")
AUTH_URL = os.getenv("AUTH_SERVICE_URL")
PROMPT_URL = os.getenv("PROMPT_SERVICE_URL")
JOURNAL_URL = os.getenv("JOURNAL_SERVICE_URL")
REDIS_URL = os.getenv("REDIS_SERVICE_URL")

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status_code"],
)
REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Histogram of request latency",
    ["method", "endpoint"],
)

@asynccontextmanager
async def lifespan(_: FastAPI):
    redis_connection = Redis.from_url("redis://localhost:6379", encoding="utf8")
    await FastAPILimiter.init(redis_connection)
    yield
    await FastAPILimiter.close()

app = FastAPI()

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    endpoint = request.url.path
    method   = request.method
    status   = response.status_code

    # observe latency
    REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(duration)
    # increment counter
    REQUEST_COUNT.labels(method=method, endpoint=endpoint, status_code=status).inc()

    return response

# Using multiprocess collector for registry
def make_metrics_app():
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
    return make_asgi_app(registry=registry)

metrics_app = make_metrics_app()
app.mount("/metrics", metrics_app)

security = HTTPBearer()

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
            f"{PROMPT_URL}/prompt",  # Docker service name + port
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

@app.get("/journals")
async def proxy_journals(
    request: Request,
    token_payload: dict = Depends(verify_jwt),
    dependencies=[Depends(RateLimiter(times=20, seconds=60))]  # Rate limit this endpoint
):
    body = await request.json()
    user_id = token_payload.get("user_id")
    if not user_id:
        raise HTTPException(401, "Invalid token payload")

    # forward to prompting service
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            f"{JOURNAL_URL}/journals",  # Docker service name + port
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