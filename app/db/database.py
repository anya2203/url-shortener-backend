from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite file will be created in the project root as "shortener.db"
SQLALCHEMY_DATABASE_URL = "sqlite:///./shortener.db"

# check_same_thread=False is required ONLY for SQLite — it lets FastAPI's
# multiple threads share the same connection safely for our use case.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Dependency that provides a DB session per request, and closes it after."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
