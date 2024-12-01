# product.py
from mongoengine import Document, StringField, FloatField, IntField

class Product(Document):
    product_id = IntField(primary_key=True)
    name = StringField(required=True, max_length=255)
    description = StringField()
    price = FloatField(required=True)
    stock_quantity = IntField(default=0)
    category = StringField()

    def __repr__(self):
        return f"<Product(product_id={self.product_id}, name={self.name}, price={self.price}, stock_quantity={self.stock_quantity})>"
