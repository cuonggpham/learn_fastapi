# repositories/fee_repository.py

from sqlalchemy.orm import Session
from app.models.fee import Fee
from app.schemas.fee import FeeCreate, FeeUpdate

def get_all_fees(db: Session):
    return db.query(Fee).all()

def get_fee_by_id(db: Session, fee_id: int):
    return db.query(Fee).filter(Fee.id == fee_id).first()

def create_fee(db: Session, fee_data: FeeCreate):
    fee = Fee(**fee_data.dict())
    db.add(fee)
    db.commit()
    db.refresh(fee)
    return fee

def update_fee(db: Session, fee_id: int, fee_data: FeeUpdate):
    fee = get_fee_by_id(db, fee_id)
    if fee:
        for key, value in fee_data.dict().items():
            setattr(fee, key, value)
        db.commit()
        db.refresh(fee)
    return fee

def delete_fee(db: Session, fee_id: int):
    fee = get_fee_by_id(db, fee_id)
    if fee:
        db.delete(fee)
        db.commit()
    return fee
