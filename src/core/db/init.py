from core import config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(config.POSTGRES_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print(str(e))
    finally:
        db.close()