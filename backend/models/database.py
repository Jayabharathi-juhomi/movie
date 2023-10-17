from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException, status
from backend.config import get_settings

settings = get_settings()
DB_USER: str = settings.DB_USER
DB_PASSWORD: str = settings.DB_PASSWORD
DB_HOST: str = settings.DB_HOST
DB_NAME: str = settings.DB_NAME

SQLALCHEMY_DATABASE_URL: str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database operation failed: " + str(e)
        )
    finally:
        db.close()
