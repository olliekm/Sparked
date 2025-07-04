from pydantic import BaseSettings, Field
from typing import Optional, List

class Settings(BaseSettings):
    
    app_name: str = Field(default="Gateway Service", env="APP_NAME")
    environment: str = Field(default="development", env="ENVIRONMENT") # production, staging, development
    version: str = Field(default="1.0.0", env="APP_VERSION")

    jwt_secret: str = Field(..., env="JWT_SECRET")
    jwt_algorithm: str = Field(default="HS256", env="JWT_ALGORITHM")
    jwt_expiration: int = Field(default=3600, env="JWT_EXPIRATION", description="JWT expiration time in seconds")

    auth_service_url: str = Field(..., env="AUTH_SERVICE_URL")
    prompt_service_url: str = Field(..., env="PROMPT_SERVICE_URL")
    journal_service_url: str = Field(..., env="JOURNAL_SERVICE_URL")
    
    redis_url: str = Field(..., env="REDIS_SERVICE_URL")

    allowed_origins: List[str] = Field(
        default=["*"],
        env="ALLOWED_ORIGINS",
        description="List of allowed CORS origins",
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    