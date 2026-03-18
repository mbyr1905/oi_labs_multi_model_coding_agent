from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from services.admin import get_users, get_products, get_orders

router = APIRouter()

@router.get('/users')
async def get_users():
    users = get_users()
    return users

@router.get('/products')
async def get_products():
    products = get_products()
    return products

@router.get('/orders')
async def get_orders():
    orders = get_orders()
    return orders