# app/database.py
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from .config import settings

DB_URL = settings.DB_URL

# Special connect args for SQLite only
connect_args = {"check_same_thread": False} if DB_URL.startswith("sqlite") else {}

# Create engine
# pool_pre_ping=True helps avoid stale connections for MySQL/Postgres.
engine = create_engine(
    DB_URL,
    pool_pre_ping=True,
    connect_args=connect_args,
)

# Session factory
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base class for models
Base = declarative_base()


# FastAPI dependency
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

