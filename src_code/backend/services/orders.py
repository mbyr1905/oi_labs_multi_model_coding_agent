from models import Order
from schemas.order import OrderCreate
from database import SessionLocal

def create_order(order: OrderCreate):
    db = SessionLocal()
    new_order = Order(customer_id=order.customer_id, product_id=order.product_id)
    db.add(new_order)
    db.commit()

def get_orders():
    db = SessionLocal()
    orders = db.query(Order).all()
    return orders