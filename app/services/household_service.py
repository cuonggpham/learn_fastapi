# app/services/household_service.py

from sqlalchemy.orm import Session
from app.models.household import Household
from app.schemas.household import HouseholdCreate, HouseholdUpdate

def create_household(db: Session, household_in: HouseholdCreate) -> Household:
    household = Household(**household_in.model_dump())
    db.add(household)
    db.commit()
    db.refresh(household)
    return household

def get_household(db: Session, household_id: int) -> Household | None:
    return db.query(Household).filter(Household.id == household_id).first()

def get_all_households(db: Session) -> list[Household]:
    return db.query(Household).all()

def update_household(db: Session, household_id: int, household_in: HouseholdUpdate) -> Household | None:
    household = get_household(db, household_id)
    if not household:
        return None
    for field, value in household_in.model_dump(exclude_unset=True).items():
        setattr(household, field, value)
    db.commit()
    db.refresh(household)
    return household

def delete_household(db: Session, household_id: int) -> bool:
    household = get_household(db, household_id)
    if not household:
        return False
    db.delete(household)
    db.commit()
    return True
