from models.category import Category
from schemas.category import CategoryCreate

class CategoryService:
    def create_category(self, category: CategoryCreate):
        new_category = Category(name=category.name)
        return new_category