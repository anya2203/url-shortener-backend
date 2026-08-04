from datetime import datetime

from pydantic import BaseModel, HttpUrl


class URLCreateRequest(BaseModel):
    original_url: HttpUrl


class URLResponse(BaseModel):
    short_code: str
    original_url: HttpUrl
    created_at: datetime
    clicks: int

    class Config:
        from_attributes = True  # allows creating this from a SQLAlchemy object
