from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from services.seller import get_products, get_orders

router = APIRouter()

@router.get('/products')
async def get_products():
    products = get_products()
    return products

@router.get('/orders')
async def get_orders():
    orders = get_orders()
    return orders