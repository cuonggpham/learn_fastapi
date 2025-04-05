# app/schemas/citizen.py

from pydantic import BaseModel
from typing import Optional

class CitizenBase(BaseModel):
    name: str
    age: int
    gender: str
    relationship: str
    household_id: int

class CitizenCreate(CitizenBase):
    pass

class CitizenUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    relationship: Optional[str] = None
    household_id: Optional[int] = None

class CitizenRead(CitizenBase):
    id: int

    class Config:
        from_attributes = True
