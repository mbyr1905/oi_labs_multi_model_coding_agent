from backend.models import Category
from backend.schemas import CategoryCreate

class CategoryService:
    def create_category(self, category: CategoryCreate):
        new_category = Category(name=category.name)
        # save to database
        return new_category
