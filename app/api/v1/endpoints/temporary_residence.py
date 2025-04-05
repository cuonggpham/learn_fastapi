from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.temporary_residence import TemporaryResidenceCreate, TemporaryResidenceRead
from app.models.temporary_residence import TemporaryResidence
from app.core.database import get_db

router = APIRouter(prefix="/temporary-residences", tags=["Temporary Residence"])

@router.post("/", response_model=TemporaryResidenceRead)
def create_temporary_residence(
    data: TemporaryResidenceCreate,
    db: Session = Depends(get_db)
):
    db_obj = TemporaryResidence(**data.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

@router.get("/", response_model=list[TemporaryResidenceRead])
def get_all(db: Session = Depends(get_db)):
    return db.query(TemporaryResidence).all()
