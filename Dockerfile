FROM python:3.13-slim

# set both env vars correctly
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
# (optional) ensure 'from app.main import app' works everywhere
ENV PYTHONPATH=/app

WORKDIR /app

# install runtime deps only
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY app ./app

# runtime dir
RUN mkdir -p /app/uploads

# choose 8000 (your current CMD) or switch to 8080 to match K8s
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]