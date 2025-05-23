from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base

class SupplierRequest(Base):
    __tablename__ = "supplier_requests"

    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id", ondelete="CASCADE"), nullable=False)
    request_id = Column(Integer, ForeignKey("purchase_requests.id", ondelete="CASCADE"), nullable=False)

    supplier = relationship("Supplier", back_populates="requests")
    purchase_request = relationship("PurchaseRequest", back_populates="supplier_links")

    __table_args__ = (
        UniqueConstraint("supplier_id", "request_id", name="uix_supplier_request"),
    )
