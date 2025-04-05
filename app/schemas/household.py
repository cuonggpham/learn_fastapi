# app/schemas/household.py

from pydantic import BaseModel
from typing import Optional

class HouseholdBase(BaseModel):
    household_code: str
    owner_name: str
    address: str
    num_members: int

class HouseholdCreate(HouseholdBase):
    pass

class HouseholdUpdate(BaseModel):
    household_code: Optional[str] = None
    owner_name: Optional[str] = None
    address: Optional[str] = None
    num_members: Optional[int] = None

class HouseholdRead(HouseholdBase):
    id: int

    class Config:
        from_attributes = True
