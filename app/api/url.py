import logging
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.url import URL
from app.schemas.url import URLCreateRequest, URLResponse
from app.core.shortener import generate_short_code

router = APIRouter()
logger = logging.getLogger("url_shortener")


@router.post("/shorten", response_model=URLResponse, status_code=201)
def create_short_url(request: URLCreateRequest, db: Session = Depends(get_db)):
    short_code = generate_short_code()
    attempts = 0
    while db.query(URL).filter(URL.short_code == short_code).first():
        short_code = generate_short_code()
        attempts += 1
        if attempts > 5:
            raise HTTPException(
                status_code=500,
                detail="Could not generate a unique short code, please try again",
            )

    db_url = URL(short_code=short_code, original_url=str(request.original_url))
    try:
        db.add(db_url)
        db.commit()
        db.refresh(db_url)
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"DB error creating short URL: {e}")
        raise HTTPException(status_code=500, detail="Failed to save URL, please try again")

    return db_url


@router.get("/{short_code}")
def redirect_to_original(short_code: str, db: Session = Depends(get_db)):
    if not short_code.strip():
        raise HTTPException(status_code=400, detail="Short code cannot be empty")

    try:
        db_url = db.query(URL).filter(URL.short_code == short_code).first()
    except SQLAlchemyError as e:
        logger.error(f"DB error during lookup: {e}")
        raise HTTPException(status_code=500, detail="Database error, please try again")

    if not db_url:
        raise HTTPException(status_code=404, detail=f"Short code '{short_code}' not found")

    try:
        db_url.clicks += 1
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.warning(f"Click count update failed (non-critical): {e}")

    return RedirectResponse(url=db_url.original_url)