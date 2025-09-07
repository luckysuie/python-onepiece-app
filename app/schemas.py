from pydantic import BaseModel, EmailStr, field_validator
class UserCreate(BaseModel):
first_name: str
last_name: str
email: EmailStr
password: str
confirm_password: str
@field_validator("email")
@classmethod
def gmail_only(cls, v: EmailStr):
if not str(v).endswith("@gmail.com"):
raise ValueError("Please use a Gmail address.")
return v
5
@field_validator("confirm_password")
@classmethod
def passwords_match(cls, v, values):
if "password" in values and v != values["password"]:
raise ValueError("Passwords do not match.")
return v
class UserOut(BaseModel):
id: int
first_name: str
last_name: str
email: EmailStr
photo_path: str | None = None
class Config:
from_attributes = True
