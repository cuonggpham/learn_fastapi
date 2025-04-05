# app/services/citizen_service.py

from sqlalchemy.orm import Session
from app.models.citizen import Citizen
from app.schemas.citizen import CitizenCreate, CitizenUpdate

def create_citizen(db: Session, citizen_in: CitizenCreate) -> Citizen:
    citizen = Citizen(**citizen_in.model_dump())
    db.add(citizen)
    db.commit()
    db.refresh(citizen)
    return citizen

def get_all_citizens(db: Session) -> list[Citizen]:
    return db.query(Citizen).all()

def get_citizen(db: Session, citizen_id: int) -> Citizen | None:
    return db.query(Citizen).filter(Citizen.id == citizen_id).first()

def update_citizen(db: Session, citizen_id: int, citizen_in: CitizenUpdate) -> Citizen | None:
    citizen = get_citizen(db, citizen_id)
    if not citizen:
        return None
    for field, value in citizen_in.model_dump(exclude_unset=True).items():
        setattr(citizen, field, value)
    db.commit()
    db.refresh(citizen)
    return citizen

def delete_citizen(db: Session, citizen_id: int) -> bool:
    citizen = get_citizen(db, citizen_id)
    if not citizen:
        return False
    db.delete(citizen)
    db.commit()
    return True
