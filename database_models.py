from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float


Base = declarative_base()

class Order(Base):

    __tablename__ = "orders"

    orderId = Column(Integer, primary_key = True, index= True)
    customerName = Column(String)
    productName = Column(String)
    quantity= Column(Integer)
    unitPrice= Column(Float) 


