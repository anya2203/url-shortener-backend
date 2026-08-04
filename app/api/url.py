from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.url import URL
from app.schemas.url import URLCreateRequest, URLResponse
from app.core.shortener import generate_short_code

router = APIRouter()


@router.post("/shorten", response_model=URLResponse, status_code=201)
def create_short_url(request: URLCreateRequest, db: Session = Depends(get_db)):
    # Generate a unique short code, retrying on the rare collision
    short_code = generate_short_code()
    while db.query(URL).filter(URL.short_code == short_code).first():
        short_code = generate_short_code()

    db_url = URL(short_code=short_code, original_url=str(request.original_url))
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url


@router.get("/{short_code}")
def redirect_to_original(short_code: str, db: Session = Depends(get_db)):
    db_url = db.query(URL).filter(URL.short_code == short_code).first()
    if not db_url:
        raise HTTPException(status_code=404, detail="Short URL not found")

    db_url.clicks += 1
    db.commit()
    return RedirectResponse(url=db_url.original_url)