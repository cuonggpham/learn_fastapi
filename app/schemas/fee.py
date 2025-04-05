# app/schemas/fee.py

from pydantic import BaseModel
from typing import Optional

class FeeBase(BaseModel):
    name: str
    amount: float
    description: Optional[str] = None

class FeeCreate(FeeBase):
    pass

class FeeUpdate(BaseModel):
    name: Optional[str] = None
    amount: Optional[float] = None
    description: Optional[str] = None

class FeeRead(FeeBase):
    id: int

    class Config:
        from_attributes = True 
