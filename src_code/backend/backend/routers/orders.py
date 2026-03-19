from fastapi import APIRouter, Depends
from backend.services.order_service import OrderService
outer = APIRouter()

@router.post("/orders")
def create_order(order: OrderCreate):
    order_service = OrderService()
    new_order = order_service.create_order(order)
    return new_order
