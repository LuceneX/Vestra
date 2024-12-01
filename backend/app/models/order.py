# order.py
from mongoengine import Document, StringField, IntField, FloatField, DateTimeField, ReferenceField
from datetime import datetime
from app.models.product import Product
from app.models.user import User

class Order(Document):
    order_id = IntField(primary_key=True)
    user = ReferenceField(User, required=True)
    product = ReferenceField(Product, required=True)
    quantity = IntField(default=1)
    status = StringField(default='pending')
    total_price = FloatField()
    created_at = DateTimeField(default=datetime.utcnow)

    def __repr__(self):
        return f"<Order(order_id={self.order_id}, user={self.user.username}, product={self.product.name}, quantity={self.quantity}, status={self.status})>"
