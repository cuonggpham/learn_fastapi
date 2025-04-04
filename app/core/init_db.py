# app/core/init_db.py

from app.core.database import engine, Base
from app.models.fee import Fee
from app.models.household import Household
from app.models.citizen import Citizen 
from app.models.temporary_absence import TemporaryAbsence
from app.models.temporary_residence import TemporaryResidence
from app.models.user import User


def init_db():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine) 
    print("Done.")

if __name__ == "__main__":
    init_db()
