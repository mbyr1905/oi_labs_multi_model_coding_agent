from backend.models import Product
from backend.schemas import ProductCreate

class ProductService:
    def create_product(self, product: ProductCreate):
        new_product = Product(name=product.name, description=product.description, price=product.price)
        # save to database
        return new_product
