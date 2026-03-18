from fastapi import APIRouter, Depends
from schemas.product import ProductCreate
from services.product_service import ProductService

router = APIRouter()

@router.post('/')
def create_product(product: ProductCreate):
    product_service = ProductService()
    new_product = product_service.create_product(product)
    return new_product