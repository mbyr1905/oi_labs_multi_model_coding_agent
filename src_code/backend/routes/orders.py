from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from schemas.order import OrderCreate
from services.orders import create_order, get_orders

router = APIRouter()

@router.post('/')
async def create_order(order: OrderCreate):
    create_order(order)
    return {'message': 'Order created successfully'}

@router.get('/')
async def get_orders():
    orders = get_orders()
    return orders