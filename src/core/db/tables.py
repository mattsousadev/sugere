from sqlalchemy import Column, Integer, String, DateTime, func, Float, ForeignKey
from sqlalchemy.orm import relationship
from .init import Base

class Nota(Base):
    __tablename__='nota'
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(255), nullable=True, index=True)
    created_at = Column(DateTime, nullable=True, server_default=func.now())
    updated_at = Column(DateTime, nullable=True, server_default=func.now(), server_onupdate=func.now())
    relationship_item = relationship('NotaItem', uselist=True )

class NotaItem(Base):
    __tablename__='nota_item'

    id = Column(Integer, primary_key=True, index=True)
    id_item = Column(String, index=True)
    nota_id = Column(Integer, ForeignKey(Nota.id), nullable=False)
    description = Column(String(255), nullable=True)
    quantity = Column(Float, nullable=True)
    unit = Column(String(255), nullable=True)
    unit_value = Column(Float, nullable=True)
    value = Column(Float, nullable=True)
    created_at = Column(DateTime, nullable=True, server_default=func.now())
    updated_at = Column(DateTime, nullable=True, server_default=func.now(), server_onupdate=func.now())