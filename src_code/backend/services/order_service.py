from models.order import Order
from schemas.order import OrderCreate

class OrderService:
    def create_order(self, order: OrderCreate):
        new_order = Order(user_id=order.user_id)
        return new_order