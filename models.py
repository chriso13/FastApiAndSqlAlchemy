from pydantic import BaseModel



class Order(BaseModel):
    orderId: int
    customerName: str
    productName: str
    quantity: int
    unitPrice: float
    
    