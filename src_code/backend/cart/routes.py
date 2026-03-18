from fastapi import APIRouter, Depends
from schemas.cart_item import CartItemCreate
from services.cart_service import CartService

router = APIRouter()

@router.post('/add')
def add_to_cart(cart_item: CartItemCreate):
    cart_service = CartService()
    new_cart_item = cart_service.create_cart_item(cart_item)
    return new_cart_item