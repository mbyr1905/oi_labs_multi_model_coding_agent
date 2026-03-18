from pydantic import BaseModel

class Category(BaseModel):
    id: int
    name: str

class CategoryCreate(BaseModel):
    name: str