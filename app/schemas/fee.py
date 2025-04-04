from pydantic import BaseModel
from typing import Optional

class FeeBase(BaseModel):
    name: str
    amount: int
    description: Optional[str] = None

class FeeCreate(FeeBase):
    pass  # dùng cho request tạo mới

class FeeOut(FeeBase):
    id: int  # dùng cho response

    class Config:
        orm_mode = True
