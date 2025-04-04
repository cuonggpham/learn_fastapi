from app.schemas.fee import FeeOut
from fastapi import HTTPException

# fake database
_fake_fees = [
    {"id": 1, "name": "Phí dịch vụ", "amount": 100000, "description": "Phí vệ sinh và an ninh"},
    {"id": 2, "name": "Phí quản lý", "amount": 150000, "description": "Phí quản lý vận hành"},
]

async def get_all_fees() -> list[FeeOut]:
    return [FeeOut(**fee) for fee in _fake_fees] 

async def get_fee_by_id(fee_id: int) -> FeeOut:
    for fee in _fake_fees:
        if fee["id"] == fee_id:
            return FeeOut(**fee)
    raise HTTPException(status_code=404, detail=f"Fee with id {fee_id} not found")
