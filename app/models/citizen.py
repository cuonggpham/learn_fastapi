# app/models/citizen.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Citizen(Base):
    __tablename__ = "citizens"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)
    relation = Column(String(50), nullable=False)
    household_id = Column(Integer, ForeignKey("households.id", ondelete="CASCADE"), nullable=False)

    household = relationship("Household", back_populates="citizens")
    temporary_residences = relationship("TemporaryResidence", back_populates="citizen", cascade="all, delete")
    temporary_absences = relationship("TemporaryAbsence", back_populates="citizen", cascade="all, delete")

