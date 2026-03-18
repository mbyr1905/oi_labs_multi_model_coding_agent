from models.order_item import OrderItem
from schemas.order_item import OrderItemCreate

class OrderItemService:
    def create_order_item(self, order_item: OrderItemCreate):
        new_order_item = OrderItem(order_id=order_item.order_id, product_id=order_item.product_id)
        return new_order_item