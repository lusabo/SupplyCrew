from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.purchase_request import PurchaseRequestCreate, PurchaseRequestRead
from app.models.purchase_request import PurchaseRequest
from app.database import get_db

router = APIRouter(
    prefix="/purchase-requests",
    tags=["purchase_requests"],
)


@router.post("/", response_model=PurchaseRequestRead)
def create_purchase_request(
    request_data: PurchaseRequestCreate,
    db: Session = Depends(get_db)
):
    purchase_request = PurchaseRequest(
        category_id=request_data.category_id,
        material_id=request_data.material_id,
        specification=request_data.specification,
        quantity=request_data.quantity,
        proposal_deadline=request_data.proposal_deadline,
        delivery_due_date=request_data.delivery_due_date,
    )
    db.add(purchase_request)
    db.commit()
    db.refresh(purchase_request)
    return purchase_request


@router.get("/", response_model=list[PurchaseRequestRead])
def list_purchase_requests(db: Session = Depends(get_db)):
    return db.query(PurchaseRequest).order_by(PurchaseRequest.id.desc()).all()


@router.get("/{request_id}", response_model=PurchaseRequestRead)
def get_purchase_request(request_id: int, db: Session = Depends(get_db)):
    purchase_request = db.query(PurchaseRequest).filter_by(id=request_id).first()
    if not purchase_request:
        raise HTTPException(status_code=404, detail="Purchase request not found")
    return purchase_request
