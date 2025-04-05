from datetime import date
from pydantic import BaseModel, ConfigDict

class TemporaryResidenceBase(BaseModel):
    start_date: date
    end_date: date | None = None
    reason: str
    address: str

class TemporaryResidenceCreate(TemporaryResidenceBase):
    citizen_id: int

class TemporaryResidenceRead(TemporaryResidenceBase):
    id: int
    citizen_id: int

    model_config = ConfigDict(from_attributes=True)
