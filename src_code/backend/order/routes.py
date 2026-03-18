from fastapi import APIRouter, Depends
from schemas.order import OrderCreate
from services.order_service import OrderService

router = APIRouter()

@router.post('/')
def create_order(order: OrderCreate):
    order_service = OrderService()
    new_order = order_service.create_order(order)
    return new_order