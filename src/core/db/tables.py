from sqlalchemy import Column, Integer, String, DateTime, func
from .init import Base

class Nota(Base):
    __tablename__='nota'
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(255), nullable=True, index=True)
    created_at = Column(DateTime, nullable=True, server_default=func.now())
    updated_at = Column(DateTime, nullable=True, server_default=func.now(), server_onupdate=func.now())
