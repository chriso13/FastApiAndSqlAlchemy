from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session

from models import Order

from config_database import engine, get_db

from order_service import get_All_Orders, ge_tOrderByOrderId, add_Order, edit_One_Order, delete_OrderBy_orderId

import database_models

database_models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/orders")
def getOrders(db: Session = Depends(get_db)):

    return get_All_Orders(db)


@app.post("/orders")
def createOrder(order: Order, db: Session=Depends(get_db)):
    return add_Order(order,db)

@app.get("/orders/{orderId}")
def getOrderById(orderId: int, db: Session=Depends(get_db)):

    return ge_tOrderByOrderId(orderId,db)


@app.put("/orders/{orderId}")
def editOrder(orderId: int, order: Order,  db: Session=Depends(get_db)):
    return edit_One_Order(orderId, order,db)


@app.delete("/orders/{orderId}")
def deleteOrderById(orderId:int,db: Session=Depends(get_db)):
    return delete_OrderBy_orderId(orderId,db)









