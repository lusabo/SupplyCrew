from sqlalchemy import (
    Column,
    Integer,
    Text,
    Date,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    email = Column(Text, nullable=False, unique=True)

    materials = relationship("SupplierMaterial", back_populates="supplier")
    requests = relationship("SupplierRequest", back_populates="supplier")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False, unique=True)


class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False, unique=True)


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
