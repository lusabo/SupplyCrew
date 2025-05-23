from pydantic import BaseModel
from datetime import date
from typing import List


class PurchaseRequestItemCreate(BaseModel):
    category_id: int
    material_id: int
    specification: str
    quantity: int


class PurchaseRequestWithItemsCreate(BaseModel):
    proposal_deadline: date
    delivery_due_date: date
    items: List[PurchaseRequestItemCreate]
