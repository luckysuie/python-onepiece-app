# app/config.py
import os
from dotenv import load_dotenv

# Load variables from a local .env file if present
load_dotenv()


class Settings:
    # ----------------------------------------------------------------------------
    # Default to SQLite for local/dev so the app runs even without a DB server.
    # >>> CHANGE AFTER MYSQL SETUP:
    # Put this in your .env (no spaces/newlines):
    # DB_URL="mysql+pymysql://appuser:StrongP@ss!@<DB_HOST>:3306/onepiece_db"
    # ----------------------------------------------------------------------------
    DB_URL: str = os.getenv("DB_URL", "sqlite:///./app.db")

    # Where uploads will be stored (keep "uploads" for local dev)
    UPLOAD_DIR: str = os.getenv("UPLOAD_DIR", "uploads")

    # App metadata
    APP_TITLE: str = os.getenv("APP_TITLE", "One Piece Registration (FastAPI)")
    APP_DEBUG: bool = os.getenv("APP_DEBUG", "true").lower() == "true"


settings = Settings()

