# app/api/v1/api.py

from fastapi import APIRouter

from .endpoints.fee import router as fee_router
from .endpoints.household import router as household_router
from .endpoints.citizen import router as citizen_router 
from .endpoints import temporary_absence, temporary_residence 
from .endpoints.auth import router as auth_router

api_router = APIRouter()
api_router.include_router(fee_router, prefix="/fees", tags=["Fees"])
api_router.include_router(household_router, prefix="/households", tags=["Households"]) 
api_router.include_router(citizen_router, prefix="/citizens", tags=["Citizens"])
api_router.include_router(temporary_residence.router)
api_router.include_router(temporary_absence.router)
api_router.include_router(auth_router)
