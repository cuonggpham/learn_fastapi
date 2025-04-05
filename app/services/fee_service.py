# app/services/fee_service.py

from sqlalchemy.orm import Session
from app.models import Fee
from app.schemas import FeeCreate, FeeUpdate

def create_fee(db: Session, fee_in: FeeCreate) -> Fee:
    fee = Fee(**fee_in.model_dump())
    db.add(fee)
    db.commit()
    db.refresh(fee)
    return fee

def get_fee(db: Session, fee_id: int) -> Fee | None:
    return db.query(Fee).filter(Fee.id == fee_id).first()

def get_all_fees(db: Session) -> list[Fee]:
    return db.query(Fee).all()

def update_fee(db: Session, fee_id: int, fee_in: FeeUpdate) -> Fee | None:
    fee = get_fee(db, fee_id)
    if not fee:
        return None
    for field, value in fee_in.model_dump(exclude_unset=True).items():
        setattr(fee, field, value)
    db.commit()
    db.refresh(fee)
    return fee

def delete_fee(db: Session, fee_id: int) -> bool:
    fee = get_fee(db, fee_id)
    if not fee:
        return False
    db.delete(fee)
    db.commit()
    return True
