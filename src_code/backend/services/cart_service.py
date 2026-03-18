from models.cart_item import CartItem
from schemas.cart_item import CartItemCreate

class CartService:
    def create_cart_item(self, cart_item: CartItemCreate):
        new_cart_item = CartItem(user_id=cart_item.user_id, product_id=cart_item.product_id)
        return new_cart_item