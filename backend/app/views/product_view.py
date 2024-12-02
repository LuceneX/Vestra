from fastapi import APIRouter, Depends, HTTPException, status
from app.services.product_service import ProductService
from app.models.product import Product, ProductCreate, ProductUpdate
from typing import List

router = APIRouter(prefix="/products", tags=["Products"])

# Dependency injection for ProductService
def get_product_service() -> ProductService:
    return ProductService()

@router.get("/", response_model=List[Product])
async def list_products(service: ProductService = Depends(get_product_service)):
    """Get a list of all products."""
    return await service.get_all_products()

@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: str, service: ProductService = Depends(get_product_service)):
    """Get a product by ID."""
    product = await service.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate, service: ProductService = Depends(get_product_service)):
    """Create a new product."""
    return await service.create_product(product)

@router.put("/{product_id}", response_model=Product)
async def update_product(
    product_id: str, product: ProductUpdate, service: ProductService = Depends(get_product_service)
):
    """Update an existing product."""
    updated_product = await service.update_product(product_id, product)
    if not updated_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return updated_product

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: str, service: ProductService = Depends(get_product_service)):
    """Delete a product."""
    success = await service.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return {"message": "Product deleted successfully"}
