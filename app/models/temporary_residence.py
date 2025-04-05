from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class TemporaryResidence(Base):
    __tablename__ = "temporary_residences"

    id = Column(Integer, primary_key=True, index=True)
    citizen_id = Column(Integer, ForeignKey("citizens.id", ondelete="CASCADE"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    reason = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)

    citizen = relationship("Citizen", back_populates="temporary_residences")
