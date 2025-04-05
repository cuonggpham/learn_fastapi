from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.temporary_absence import TemporaryAbsenceCreate, TemporaryAbsenceRead
from app.models.temporary_absence import TemporaryAbsence
from app.core.database import get_db

router = APIRouter(prefix="/temporary-absences", tags=["Temporary Absence"])

@router.post("/", response_model=TemporaryAbsenceRead)
def create_temporary_absence(
    data: TemporaryAbsenceCreate,
    db: Session = Depends(get_db)
):
    db_obj = TemporaryAbsence(**data.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

@router.get("/", response_model=list[TemporaryAbsenceRead])
def get_all(db: Session = Depends(get_db)):
    return db.query(TemporaryAbsence).all()
