from backend.models import Order
from backend.schemas import OrderCreate

class OrderService:
    def create_order(self, order: OrderCreate):
        new_order = Order(user_id=order.user_id, total=order.total)
        # save to database
        return new_order
