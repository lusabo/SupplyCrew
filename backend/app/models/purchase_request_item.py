from sqlalchemy import Column, Integer, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class PurchaseRequestItem(Base):
    __tablename__ = "purchase_request_items"

    id = Column(Integer, primary_key=True)
    purchase_request_id = Column(Integer, ForeignKey("purchase_requests.id", ondelete="CASCADE"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    material_id = Column(Integer, ForeignKey("materials.id"), nullable=False)
    specification = Column(Text, nullable=False)
    quantity = Column(Integer, nullable=False)

    purchase_request = relationship("PurchaseRequest", back_populates="items")

