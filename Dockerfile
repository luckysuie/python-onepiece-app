FROM python:3.13-slim
ENV PYTHONDONTWRITEBYTECODE=1
PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# Copy app code
COPY app ./app
# Create uploads dir at runtime (also mounted by docker-compose)
RUN mkdir -p /app/uploads
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

