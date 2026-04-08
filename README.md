# 🚀 StockFlow - Inventory Management Backend API

A backend system built using FastAPI for managing inventory across warehouses. This project demonstrates REST API development, database integration, and scalable backend architecture.


- Add new products
- View all products
- Update product details
- Delete products

It is designed with clean architecture and RESTful APIs to demonstrate backend engineering skills.

---

## 🛠 Tech Stack

- **Python**
- **FastAPI**
- **SQLAlchemy (ORM)**
- **SQLite (can be switched to MySQL)**
- **Uvicorn**

---

## 📂 Project Structure


stockflow-backend/
│
├── app/
│ ├── main.py
│ ├── models.py
│ ├── database.py
│ ├── schemas.py
│ └── routes/
│ └── product.py
│
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository


git clone https://github.com/rupeshsonawane00012/bynry-backend-case-study.git

cd bynry-backend-case-study


---

### 2️⃣ Create virtual environment


python -m venv venv
venv\Scripts\activate


---

### 3️⃣ Install dependencies


pip install -r requirements.txt


---

### 4️⃣ Run the server


uvicorn app.main:app --reload


---

## 📡 API Documentation

FastAPI automatically provides interactive API docs:

👉 http://127.0.0.1:8000/docs  

You can test all endpoints directly from the browser.

---

## 🧪 API Endpoints

### ➕ Create Product
POST `/products`

```json
{
  "name": "Laptop",
  "quantity": 10,
  "price": 50000
}
📋 Get All Products

GET /products

✏️ Update Product

PUT /products/{id}

❌ Delete Product

DELETE /products/{id}

💡 Features
RESTful API design
Full CRUD operations
Database integration using ORM
Clean and modular project structure
Auto-generated Swagger documentation

So now database location and tables itself using SqlAlchemy ORM's database.create_all()<(), Please safe it to your directory once
it is executed, it is going to create tables by own

Swagger documentation will help you test all endpointsricesl
🔄 Database

Currently using SQLite for simplicity.
Can be easily switched to MySQL by updating the database connection string.

🚀 Future Improvements
JWT Authentication
Role-based access control
Multi-warehouse support
Docker deployment
Cloud deployment (AWS)

