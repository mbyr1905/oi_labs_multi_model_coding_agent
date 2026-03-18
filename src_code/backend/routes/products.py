from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from schemas.product import ProductCreate
from services.products import create_product, get_products

router = APIRouter()

@router.post('/')
async def create_product(product: ProductCreate):
    create_product(product)
    return {'message': 'Product created successfully'}

@router.get('/')
async def get_products():
    products = get_products()
    return products