# services/product_service.py
from app.models.product import Product
from typing import List

def create_product(name: str, description: str, price: float, stock: int):
    """Create a new product."""
    product = Product(name=name, description=description, price=price, stock=stock)
    product.save()
    return product

def update_product(product_id: str, name: str = None, description: str = None, price: float = None, stock: int = None):
    """Update details of an existing product."""
    product = Product.objects.get(id=product_id)
    if product:
        if name:
            product.name = name
        if description:
            product.description = description
        if price is not None:
            product.price = price
        if stock is not None:
            product.stock = stock
        product.save()
        return product
    else:
        raise ValueError("Product not found")

def get_product_by_id(product_id: str):
    """Get a product by its ID."""
    product = Product.objects.get(id=product_id)
    if product:
        return product
    else:
        raise ValueError("Product not found")

def get_all_products() -> List[Product]:
    """Get all products."""
    return Product.objects.all()

def delete_product(product_id: str):
    """Delete a product."""
    product = Product.objects.get(id=product_id)
    if product:
        product.delete()
        return {"message": "Product deleted successfully"}
    else:
        raise ValueError("Product not found")
