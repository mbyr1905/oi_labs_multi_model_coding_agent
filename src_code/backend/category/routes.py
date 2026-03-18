from fastapi import APIRouter, Depends
from schemas.category import CategoryCreate
from services.category_service import CategoryService

router = APIRouter()

@router.post('/')
def create_category(category: CategoryCreate):
    category_service = CategoryService()
    new_category = category_service.create_category(category)
    return new_category