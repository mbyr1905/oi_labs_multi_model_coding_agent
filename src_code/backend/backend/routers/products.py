from fastapi import APIRouter, Depends
from backend.services.product_service import ProductService
outer = APIRouter()

@router.post("/products")
def create_product(product: ProductCreate):
    product_service = ProductService()
    new_product = product_service.create_product(product)
    return new_product
