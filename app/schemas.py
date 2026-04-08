from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    quantity: int
    price: int

class ProductResponse(ProductCreate):
    id: int

    class Config:
        orm_mode = True