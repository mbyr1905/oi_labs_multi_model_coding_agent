from fastapi import APIRouter, Depends
from backend.services import OrderService

router = APIRouter()

@router.get("/orders")
def get_orders():
    order_service = OrderService()
    orders = order_service.get_orders()
    return orders
