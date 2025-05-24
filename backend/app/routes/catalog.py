from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.category import Category
from app.models.material import Material
from app.database import get_db

router = APIRouter()

@router.get("/categories/")
def list_categories(db: Session = Depends(get_db)):
    return db.query(Category).order_by(Category.description).all()

@router.get("/materials/")
def list_materials(db: Session = Depends(get_db)):
    return db.query(Material).order_by(Material.description).all()
