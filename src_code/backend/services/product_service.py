from models.product import Product
from schemas.product import ProductCreate

class ProductService:
    def create_product(self, product: ProductCreate):
        new_product = Product(name=product.name, description=product.description, price=product.price)
        return new_product