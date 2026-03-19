from backend.models.product import Product
from backend.schemas.product import ProductCreate

class ProductService:
    def create_product(self, product: ProductCreate):
        new_product = Product(name=product.name, price=product.price, description=product.description)
        # save to database
        return new_product
