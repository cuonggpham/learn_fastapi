# app/core/init_db.py

from app.core.database import engine, Base
from app.models.fee import Fee

def init_db():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine) 
    print("Done.")

if __name__ == "__main__":
    init_db()
