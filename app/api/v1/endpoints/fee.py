# app/api/v1/endpoints/fee.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas import FeeCreate, FeeRead, FeeUpdate
from app.services.fee_service import (
    create_fee, get_all_fees, get_fee, update_fee, delete_fee
)

router = APIRouter()

@router.post("/", response_model=FeeRead)
def create_fee_endpoint(fee_in: FeeCreate, db: Session = Depends(get_db)):
    return create_fee(db, fee_in)

@router.get("/", response_model=list[FeeRead])
def get_all_fees_endpoint(db: Session = Depends(get_db)):
    return get_all_fees(db)

@router.get("/{fee_id}", response_model=FeeRead)
def get_fee_by_id(fee_id: int, db: Session = Depends(get_db)):
    fee = get_fee(db, fee_id)
    if not fee:
        raise HTTPException(status_code=404, detail="Fee not found")
    return fee

@router.put("/{fee_id}", response_model=FeeRead)
def update_fee_endpoint(fee_id: int, fee_in: FeeUpdate, db: Session = Depends(get_db)):
    fee = update_fee(db, fee_id, fee_in)
    if not fee:
        raise HTTPException(status_code=404, detail="Fee not found")
    return fee

@router.delete("/{fee_id}")
def delete_fee_endpoint(fee_id: int, db: Session = Depends(get_db)):
    success = delete_fee(db, fee_id)
    if not success:
        raise HTTPException(status_code=404, detail="Fee not found")
    return {"message": "Fee deleted successfully"}
