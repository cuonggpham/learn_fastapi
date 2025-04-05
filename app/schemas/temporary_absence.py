from datetime import date
from pydantic import BaseModel, ConfigDict

class TemporaryAbsenceBase(BaseModel):
    start_date: date
    end_date: date | None = None
    reason: str

class TemporaryAbsenceCreate(TemporaryAbsenceBase):
    citizen_id: int

class TemporaryAbsenceRead(TemporaryAbsenceBase):
    id: int
    citizen_id: int

    model_config = ConfigDict(from_attributes=True)
