from fastapi import FastAPI
from app.database import engine, Base
from app.routes import product

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(product.router)
@app.get("/")
def home():
    return {"message": "StockFlow API is running 🚀"}