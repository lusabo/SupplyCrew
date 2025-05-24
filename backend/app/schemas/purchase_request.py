from datetime import date
from pydantic import BaseModel, Field


class PurchaseRequestCreate(BaseModel):
    category_id: int
    material_id: int
    specification: str
    quantity: int = Field(gt=0)
    proposal_deadline: date  # Aceita formato ISO 8601: YYYY-MM-DD
    delivery_due_date: date


class PurchaseRequestRead(BaseModel):
    id: int
    category_id: int
    material_id: int
    specification: str
    quantity: int
    proposal_deadline: date
    delivery_due_date: date

    class Config:
        from_attributes = True
