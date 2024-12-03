from typing import List
from pydantic import BaseModel

class OrderItem(BaseModel):
    product_id: int
    quantity: int

class Order(BaseModel):
    id: int
    user_id: int
    items: List[OrderItem]
    total_price: float
