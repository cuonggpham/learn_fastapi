from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Chào mừng đến với API Quản lý Sản phẩm!"}

@app.get("/status")
def get_status():
    return {"status": "running", "version": "1.0.0"} 

@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {"product_id": product_id, "message": "Thông tin sản phẩm"} 

@app.get("/search")
def search_product(keyword: str, limit: int = 10):
    return {"keyword": keyword, "limit": limit, "message": "Kết quả tìm kiếm"} 

@app.get("/users/{user_id}")
def get_users(user_id: int):
    return {"user_id": user_id, "name": "User X"}

orders_data = [
    {"order_id": 1, "status": "pending", "product": "Laptop"},
    {"order_id": 2, "status": "completed", "product": "Phone"},
    {"order_id": 3, "status": "pending", "product": "Tablet"},
] 

@app.get("/orders")
def get_orders(status: Optional[str] = None):
    if status:
        # Lọc đơn hàng theo trạng thái
        filtered_orders = [order for order in orders_data if order["status"] == status]
        return {"status": status, "orders": filtered_orders}
    return {"orders": orders_data}