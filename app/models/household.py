# app/models/household.py

from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Household(Base):
    __tablename__ = "households"

    id = Column(Integer, primary_key=True, index=True)
    household_code = Column(String(50), unique=True, index=True, nullable=False)
    owner_name = Column(String(100), nullable=False)
    address = Column(String(255), nullable=False)
    num_members = Column(Integer, default=1)
