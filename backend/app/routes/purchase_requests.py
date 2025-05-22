from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.models import PurchaseRequest
from app.schemas import PurchaseRequestBatch
from app.database import get_db  # função que retorna sessão do banco

router = APIRouter()


@router.post("/purchase-requests/")
def create_purchase_requests(batch: PurchaseRequestBatch, db: Session = Depends(get_db)):
    try:
        for item in batch.requests:
            proposal_deadline = datetime.strptime(item.proposal_deadline, "%d/%m/%Y").date()
            delivery_due_date = datetime.strptime(item.delivery_due_date, "%d/%m/%Y").date()

            purchase = PurchaseRequest(
                category_id=item.category_id,
                material_id=item.material_id,
                specification=item.specification,
                quantity=item.quantity,
                proposal_deadline=proposal_deadline,
                delivery_due_date=delivery_due_date
            )

            db.add(purchase)

        db.commit()
        return {"message": f"{len(batch.requests)} pedido(s) criado(s) com sucesso"}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao criar pedidos: {e}")
