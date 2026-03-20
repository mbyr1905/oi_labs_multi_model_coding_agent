from pydantic import BaseModel

class Order(BaseModel):
    id: int
    user_id: int
    total: float

class OrderCreate(BaseModel):
    user_id: int
    total: float
