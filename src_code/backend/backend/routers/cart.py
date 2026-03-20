from fastapi import APIRouter, Depends
from backend.services import CartService
from backend.schemas import CartItemCreate

router = APIRouter()

@router.post("/cart")
def create_cart_item(cart_item: CartItemCreate):
    cart_service = CartService()
    new_cart_item = cart_service.create_cart_item(cart_item)
    return new_cart_item
