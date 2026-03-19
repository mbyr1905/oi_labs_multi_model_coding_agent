from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str

class ProductCreate(BaseModel):
    name: str
    price: float
    description: str
