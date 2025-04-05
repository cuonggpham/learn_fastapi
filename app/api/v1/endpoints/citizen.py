# app/api/v1/endpoints/citizen.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.citizen import CitizenCreate, CitizenRead, CitizenUpdate
from app.services.citizen_service import (
    create_citizen, get_all_citizens, get_citizen, update_citizen, delete_citizen
)

router = APIRouter()

@router.post("/", response_model=CitizenRead)
def create_citizen_endpoint(citizen_in: CitizenCreate, db: Session = Depends(get_db)):
    return create_citizen(db, citizen_in)

@router.get("/", response_model=list[CitizenRead])
def get_all_citizens_endpoint(db: Session = Depends(get_db)):
    return get_all_citizens(db)

@router.get("/{citizen_id}", response_model=CitizenRead)
def get_citizen_endpoint(citizen_id: int, db: Session = Depends(get_db)):
    citizen = get_citizen(db, citizen_id)
    if not citizen:
        raise HTTPException(status_code=404, detail="Citizen not found")
    return citizen

@router.put("/{citizen_id}", response_model=CitizenRead)
def update_citizen_endpoint(citizen_id: int, citizen_in: CitizenUpdate, db: Session = Depends(get_db)):
    citizen = update_citizen(db, citizen_id, citizen_in)
    if not citizen:
        raise HTTPException(status_code=404, detail="Citizen not found")
    return citizen

@router.delete("/{citizen_id}")
def delete_citizen_endpoint(citizen_id: int, db: Session = Depends(get_db)):
    success = delete_citizen(db, citizen_id)
    if not success:
        raise HTTPException(status_code=404, detail="Citizen not found")
    return {"message": "Citizen deleted successfully"}
