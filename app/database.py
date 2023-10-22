# SQLALCHEMY_DATABASE_URL =
# "postgresql://<username>:<password>@<ip-address>/hostname:5432/<database-name>"
from os import getenv

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

USERNAME = getenv("POSTGRES_USER")
HOST = getenv("POSTGRES_HOST")
DB = getenv("POSTGRES_DB")


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
