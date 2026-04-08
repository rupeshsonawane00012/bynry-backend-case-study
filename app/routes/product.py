from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/products")
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

@router.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    db.delete(product)
    db.commit()
    return {"message": "Deleted"}
@router.put("/products/{id}")
def update_product(id: int, updated_product: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    
    if not product:
        return {"error": "Product not found"}

    product.name = updated_product.name
    product.quantity = updated_product.quantity
    product.price = updated_product.price

    db.commit()
    db.refresh(product)

    return product