from backend.models import CartItem
from backend.schemas import CartItemCreate

class CartService:
    def create_cart_item(self, cart_item: CartItemCreate):
        new_cart_item = CartItem(product_id=cart_item.product_id, user_id=cart_item.user_id, quantity=cart_item.quantity)
        # save to database
        return new_cart_item
