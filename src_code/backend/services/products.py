from models import Product
from schemas.product import ProductCreate
from database import SessionLocal

def create_product(product: ProductCreate):
    db = SessionLocal()
    new_product = Product(title=product.title, description=product.description, price=product.price)
    db.add(new_product)
    db.commit()

def get_products():
    db = SessionLocal()
    products = db.query(Product).all()
    return products