from sqlalchemy.orm import Session
from . import models
from .utils import hash_password
class EmailAlreadyExists(Exception):
pass
def create_user(db: Session, *, first_name: str, last_name: str, email: str,
password: str, photo_path: str | None) -> models.User:
# Check unique email
if db.query(models.User).filter(models.User.email == email).first():
raise EmailAlreadyExists()
user = models.User(
first_name=first_name,
last_name=last_name,
email=email,
password_hash=hash_password(password),
photo_path=photo_path,
)
db.add(user)
db.commit()
db.refresh(user)
return user

