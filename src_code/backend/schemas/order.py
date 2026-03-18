from pydantic import BaseModel

class Order(BaseModel):
    id: int
    user_id: int

class OrderCreate(BaseModel):
    user_id: int