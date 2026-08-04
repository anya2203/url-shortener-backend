from fastapi import FastAPI

from app.db.database import Base, engine
from app.api.url import router as url_router

# Create tables on startup (fine for SQLite/dev; in real prod you'd use Alembic migrations)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="URL Shortener API",
    description="A production-style URL shortener backend built with FastAPI.",
    version="1.0.0",
)

app.include_router(url_router, tags=["URLs"])


@app.get("/")
def root():
    return {"message": "URL Shortener API is running"}