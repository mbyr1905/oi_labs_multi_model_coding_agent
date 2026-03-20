from fastapi import APIRouter, Depends
from backend.services import CategoryService
from backend.schemas import CategoryCreate

router = APIRouter()

@router.post("/categories")
def create_category(category: CategoryCreate):
    category_service = CategoryService()
    new_category = category_service.create_category(category)
    return new_category
