from fastapi import APIRouter
from app.api.v1.endpoints import fee

api_router = APIRouter()
api_router.include_router(fee.router)
