# app/models/fee.py

from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Fee(Base):
    __tablename__ = "fees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    amount = Column(Integer, nullable=False)
    description = Column(String(500), nullable=True)
