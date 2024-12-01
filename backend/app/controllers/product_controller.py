from fastapi import APIRouter, HTTPException
from app.services.product_service import ProductService
from app.models.product import Product, ProductCreate, ProductUpdate
from typing import List

router = APIRouter()

# Initialize service
product_service = ProductService()

@router.post("/products/", response_model=Product)
async def create_product(product: ProductCreate):
    try:
        return await product_service.create_product(product)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: str):
    product = await product_service.get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: str, product: ProductUpdate):
    updated_product = await product_service.update_product(product_id, product)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/products/{product_id}")
async def delete_product(product_id: str):
    success = await product_service.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
