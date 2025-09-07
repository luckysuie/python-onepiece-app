import os
from dotenv import load_dotenv
load_dotenv()
class Settings:
DB_URL: str = os.getenv("DB_URL", "mysql+pymysql://
appuser:StrongPass@localhost:3306/onepiecedb")
UPLOAD_DIR: str = os.getenv("UPLOAD_DIR", "/app/uploads")
APP_TITLE: str = os.getenv("APP_TITLE", "One Piece Registration (FastAPI)")
APP_DEBUG: bool = os.getenv("APP_DEBUG", "false").lower() == "true"
settings = Settings()
