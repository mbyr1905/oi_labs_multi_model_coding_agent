from pydantic import BaseModel

class OrderItem(BaseModel):
    id: int
    order_id: int
    product_id: int

class OrderItemCreate(BaseModel):
    order_id: int
    product_id: int