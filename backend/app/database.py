import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Create the database connection from .env variable
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

#Using the engine, create a Session Factory
SessionLocal = sessionmaker(bind=engine)

#Used as a base class for all database models
Base = declarative_base()

def get_db():
    db = SessionLocal()

    try: 
        yield db
    finally:
        db.close()


def test_db_connection():
    try:
        db = SessionLocal()
        db.execute("SELECT 1").fetchone()
        db.close()
        print("Database connection successful!")
        return True
    except Exception as e:
        print(f"Database Connection Failed {e}")
        return False