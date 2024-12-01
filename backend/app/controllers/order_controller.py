from fastapi import APIRouter, HTTPException
from app.services.order_service import OrderService
from app.models.order import Order, OrderCreate, OrderUpdate
from typing import List

router = APIRouter()

# Initialize service
order_service = OrderService()

@router.post("/orders/", response_model=Order)
async def create_order(order: OrderCreate):
    try:
        return await order_service.create_order(order)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: str):
    order = await order_service.get_order(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: str, order: OrderUpdate):
    updated_order = await order_service.update_order(order_id, order)
    if updated_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated_order
