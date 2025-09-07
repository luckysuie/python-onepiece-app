from pathlib import Path
from fastapi import FastAPI, Request, Depends, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .config import settings
from .database import Base, engine, get_db
from .crud import create_user, EmailAlreadyExists
from .utils import saved_filename
# Create tables (like JPA ddl-auto=update for simple cases)
Base.metadata.create_all(bind=engine)
app = FastAPI(title=settings.APP_TITLE, debug=settings.APP_DEBUG)
BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
UPLOAD_DIR = Path(settings.UPLOAD_DIR)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
@app.get("/health")
def health():
return {"status": "ok"}
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
return templates.TemplateResponse("index.html", {"request": request,
"success": False})
@app.post("/submit", response_class=HTMLResponse)
async def submit(
request: Request,
firstName: str = Form(...),
lastName: str = Form(...),
email: str = Form(...),
password: str = Form(...),
confirmPassword: str = Form(...),
photo: UploadFile = File(...),
db: Session = Depends(get_db),
):
# Frontend validates, but re-validate on server for safety
if not email.endswith("@gmail.com"):
return templates.TemplateResponse("index.html", {"request": request,
"error": "Please use a Gmail address.", "success": False})
if password != confirmPassword:
return templates.TemplateResponse("index.html", {"request": request,
"error": "Passwords do not match.", "success": False})
# Save photo securely
filename = saved_filename(photo.filename)
filepath = UPLOAD_DIR / filename
with open(filepath, "wb") as f:
f.write(await photo.read())
try:
_ = create_user(
db,
first_name=firstName,
last_name=lastName,
email=email,
password=password,
photo_path=str(filepath),
)
except EmailAlreadyExists:
return templates.TemplateResponse("index.html", {"request": request,
"error": "Email already registered.", "success": False})
# Render the same template but show the welcome panel
8
return templates.TemplateResponse("index.html", {"request": request,
"success": True, "first_name": firstName})

