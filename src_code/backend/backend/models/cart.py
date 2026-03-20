from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class CartItem(Base):
    __tablename__ = 'cart_items'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    user_id = Column(Integer)
    quantity = Column(Integer)
