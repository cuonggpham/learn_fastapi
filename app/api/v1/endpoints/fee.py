# api/v1/fee.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.fee import FeeCreate, FeeRead, FeeUpdate, FeeOut
from app.services import fee_service
from app.core.database import get_db
from app.core.exceptions import CustomException, ResourceNotFoundException 

router = APIRouter(prefix="/fees", tags=["Fees"])

@router.get("/", response_model=list[FeeOut])
def list_fees(db: Session = Depends(get_db)):
    return fee_service.get_fees(db)

@router.post("/", response_model=FeeRead)
def create_fee(fee_in: FeeCreate, db: Session = Depends(get_db)):
    return {
        "id": 1,
        "name": fee_in.name,
        "amount": fee_in.amount,
        "description": fee_in.description
    }

@router.get("/{fee_id}", response_model=FeeOut)
def get_fee(fee_id: int, db: Session = Depends(get_db)):
    fee = fee_service.get_fee(db, fee_id)
    if not fee:
        raise HTTPException(status_code=404, detail="Fee not found")
    return fee

@router.put("/{fee_id}", response_model=FeeOut)
def update_fee(fee_id: int, fee: FeeUpdate, db: Session = Depends(get_db)):
    updated = fee_service.update_fee(db, fee_id, fee)
    if not updated:
        raise HTTPException(status_code=404, detail="Fee not found")
    return updated

@router.delete("/{fee_id}")
def delete_fee(fee_id: int, db: Session = Depends(get_db)):
    deleted = fee_service.delete_fee(db, fee_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Fee not found")
    return {"message": "Fee deleted"} 

