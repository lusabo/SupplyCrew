from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base

class SupplierMaterial(Base):
    __tablename__ = "supplier_materials"

    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id", ondelete="CASCADE"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    material_id = Column(Integer, ForeignKey("materials.id", ondelete="CASCADE"), nullable=False)

    supplier = relationship("Supplier", back_populates="materials")

    __table_args__ = (
        UniqueConstraint("supplier_id", "category_id", "material_id", name="uix_supplier_category_material"),
    )
