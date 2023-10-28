from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings

USERNAME = settings.POSTGRES_USER
HOST = settings.POSTGRES_HOST
DB = settings.POSTGRES_DB


SQLALCHEMY_DATABASE_URL = f"postgresql://{USERNAME}@{HOST}/{DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
