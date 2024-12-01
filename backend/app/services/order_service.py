# services/order_service.py
from app.models.order import Order
from app.models.product import Product
from app.models.user import User
from typing import List

def create_order(user: User, product_ids: List[str]):
    """Create an order for a user."""
    products = Product.objects(id__in=product_ids)
    if not products:
        raise ValueError("Products not found")

    order = Order(user=user, products=products, status="Pending")
    order.save()
    return order

def update_order_status(order_id: str, status: str):
    """Update the status of an order."""
    order = Order.objects.get(id=order_id)
    if order:
        order.status = status
        order.save()
        return order
    else:
        raise ValueError("Order not found")

def get_orders_for_user(user: User):
    """Get all orders for a specific user."""
    return Order.objects(user=user)
