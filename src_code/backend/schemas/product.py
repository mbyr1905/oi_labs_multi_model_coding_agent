from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: int

class ProductCreate(BaseModel):
    name: str
    description: str
    price: int