from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings
engine = create_engine(settings.DB_URL, pool_pre_ping=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine,
future=True)
Base = declarative_base()
# Dependency for FastAPI routes
from typing import Generator
def get_db() -> Generator:
db = SessionLocal()
try:
yield db
finally:
db.close()
