from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from models import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='products')