# app/core/config.py

from pydantic import Field
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    PROJECT_NAME: str = "BlueMoon Apartment Manager"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True
    DATABASE_URL: str = Field(..., alias="DATABASE_URL")


    class Config:
        extra = "forbid"
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
