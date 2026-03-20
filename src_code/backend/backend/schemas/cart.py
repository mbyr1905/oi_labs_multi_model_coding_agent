from pydantic import BaseModel

class CartItem(BaseModel):
    id: int
    product_id: int
    user_id: int
    quantity: int

class CartItemCreate(BaseModel):
    product_id: int
    quantity: int
