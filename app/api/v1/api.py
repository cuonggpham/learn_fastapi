# app/api/v1/api.py

from fastapi import APIRouter

from .endpoints.fee import router as fee_router
from .endpoints.household import router as household_router

api_router = APIRouter()
api_router.include_router(fee_router, prefix="/fees", tags=["Fees"])
api_router.include_router(household_router, prefix="/households", tags=["Households"])

