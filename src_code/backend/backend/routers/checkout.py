from fastapi import APIRouter, Depends
from backend.services import OrderService
from backend.schemas import OrderCreate

router = APIRouter()

@router.post("/checkout")
def create_order(order: OrderCreate):
    order_service = OrderService()
    new_order = order_service.create_order(order)
    return new_order
