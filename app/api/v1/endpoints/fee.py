# app/api/v1/endpoints/fee.py

from fastapi import APIRouter
from typing import List
from app.schemas.fee import FeeOut
from app.services.fee_service import get_all_fees, get_fee_by_id

router = APIRouter(
    prefix="/fees",
    tags=["Fees"]
)

@router.get("/", response_model=List[FeeOut])
async def get_fees():
    return await get_all_fees()

@router.get("/{fee_id}", response_model=FeeOut)
async def get_fee(fee_id: int):
    return await get_fee_by_id(fee_id)
