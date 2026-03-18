from models import User, Product, Order
from database import SessionLocal

def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    return users

def get_products():
    db = SessionLocal()
    products = db.query(Product).all()
    return products

def get_orders():
    db = SessionLocal()
    orders = db.query(Order).all()
    return orders