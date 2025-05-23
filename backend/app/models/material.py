from sqlalchemy import Column, Integer, Text
from .base import Base

class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False, unique=True)
