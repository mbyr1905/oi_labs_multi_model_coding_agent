from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    title: str
    description: str
    price: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True