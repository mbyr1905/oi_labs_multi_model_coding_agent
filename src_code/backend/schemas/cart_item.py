from pydantic import BaseModel

class CartItem(BaseModel):
    id: int
    user_id: int
    product_id: int

class CartItemCreate(BaseModel):
    user_id: int
    product_id: int