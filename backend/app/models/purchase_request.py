from sqlalchemy import Column, Integer, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
class PurchaseRequest(Base):
    __tablename__ = "purchase_requests"

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    material_id = Column(Integer, ForeignKey("materials.id"), nullable=False)
    specification = Column(Text, nullable=False)
    quantity = Column(Integer, nullable=False)
    proposal_deadline = Column(Date, nullable=False)
    delivery_due_date = Column(Date, nullable=False)

    supplier_links = relationship("SupplierRequest", back_populates="purchase_request")