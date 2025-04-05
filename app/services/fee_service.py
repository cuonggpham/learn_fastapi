# services/fee_service.py

from sqlalchemy.orm import Session
from app.schemas.fee import FeeCreate, FeeUpdate
from app.repositories import fee_repository

def get_fees(db: Session):
    return fee_repository.get_all_fees(db)

def get_fee(db: Session, fee_id: int):
    return fee_repository.get_fee_by_id(db, fee_id)

def create_fee(db: Session, fee_data: FeeCreate):
    return fee_repository.create_fee(db, fee_data)

def update_fee(db: Session, fee_id: int, fee_data: FeeUpdate):
    return fee_repository.update_fee(db, fee_id, fee_data)

def delete_fee(db: Session, fee_id: int):
    return fee_repository.delete_fee(db, fee_id)
