from pydantic import BaseModel, Field
from typing import List
from datetime import date


class PurchaseRequestCreate(BaseModel):
    category_id: int
    material_id: int
    specification: str
    quantity: int = Field(gt=0)
    proposal_deadline: str  # formato DD/MM/YYYY
    delivery_due_date: str  # formato DD/MM/YYYY


class PurchaseRequestBatch(BaseModel):
    requests: List[PurchaseRequestCreate]
