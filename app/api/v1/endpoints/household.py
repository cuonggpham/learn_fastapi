# app/api/v1/endpoints/household.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.user import User
from app.schemas.household import HouseholdCreate, HouseholdRead, HouseholdUpdate
from app.services.household_service import (
    create_household, get_all_households, get_household, update_household, delete_household
)

router = APIRouter()

@router.post("/", response_model=HouseholdRead)
def create_household_endpoint(household_in: HouseholdCreate, db: Session = Depends(get_db)):
    return create_household(db, household_in)

@router.get("/", response_model=list[HouseholdRead])
def get_all_households_endpoint(db: Session = Depends(get_db)):
    return get_all_households(db)

@router.get("/{household_id}", response_model=HouseholdRead)
def get_household_by_id(household_id: int, db: Session = Depends(get_db) ):
    household = get_household(db, household_id)
    if not household:
        raise HTTPException(status_code=404, detail="Household not found")
    return household

@router.put("/{household_id}", response_model=HouseholdRead)
def update_household_endpoint(household_id: int, household_in: HouseholdUpdate, db: Session = Depends(get_db)):
    household = update_household(db, household_id, household_in)
    if not household:
        raise HTTPException(status_code=404, detail="Household not found")
    return household

@router.delete("/{household_id}")
def delete_household_endpoint(household_id: int, db: Session = Depends(get_db)):
    success = delete_household(db, household_id)
    if not success:
        raise HTTPException(status_code=404, detail="Household not found")
    return {"message": "Household deleted successfully"}
