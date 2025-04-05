# schemas/fee.py

from typing import Optional
from pydantic import BaseModel, Field

class FeeCreate(BaseModel):
    name: str = Field(..., example="Phí dịch vụ")
    amount: float = Field(..., example=25000.0)
    description: Optional[str] = Field(None, example="Phí vệ sinh hàng tháng") 

class FeeRead(FeeCreate):
    id: int

    class Config:
        from_attributes = True

class FeeUpdate(BaseModel):
    name: str
    amount: float
    type: str

class FeeOut(BaseModel):
    id: int
    name: str
    amount: float
    type: str

    class Config:
        from_attributes = True
