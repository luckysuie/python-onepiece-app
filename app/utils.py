import os
import uuid
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str) -> str:
return pwd_context.hash(password)
# Very safe filename generator (no user-provided filename is trusted)
def saved_filename(original: str) -> str:
_ext = os.path.splitext(original)[1]
return f"{uuid.uuid4().hex}{_ext}"
