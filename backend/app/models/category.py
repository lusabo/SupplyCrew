from sqlalchemy import Column, Integer, Text
from .base import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False, unique=True)
