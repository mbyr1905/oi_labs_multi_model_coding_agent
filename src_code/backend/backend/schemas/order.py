from pydantic import BaseModel
from datetime import datetime

class Order(BaseModel):
    id: int
    user_id: int
    order_date: datetime
    total: float

class OrderCreate(BaseModel):
    user_id: int
    total: float
