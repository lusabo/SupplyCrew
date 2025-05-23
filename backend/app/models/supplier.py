from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship
from .base import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    email = Column(Text, nullable=False, unique=True)

    materials = relationship("SupplierMaterial", back_populates="supplier")
    requests = relationship("SupplierRequest", back_populates="supplier")
