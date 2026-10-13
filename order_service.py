from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session

from models import Order

from config_database import engine, get_db

import database_models

database_models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_All_Orders(db: Session):
    orders = db.query(database_models.Order).all()

    return orders

def ge_tOrderByOrderId(orderId: int, db: Session):

    findOders = db.query(database_models.Order).filter(database_models.Order.orderId==orderId).first()
    if findOders:
        return findOders

    else:

        return f"Order {orderId} not found"

def add_Order(order: Order, db: Session):
    db.add(database_models.Order(**order.model_dump()))
    db.commit()
    return {"message": "Product created successfully", "order": order}



def edit_One_Order(orderId: int, order: Order,  db: Session):
    findOders = db.query(database_models.Order).filter(database_models.Order.orderId==orderId).first()
    if findOders:
        findOders.customerName = order.customerName
        findOders.productName   = order.productName
        findOders.quantity = order.quantity
        findOders.unitPrice = order.unitPrice

        db.commit()
        db.refresh(findOders)
        return {"message": "Product edited successfully", "order": findOders}
    else:

        return f"Order {orderId} not found"


def delete_OrderBy_orderId(orderId:int,db: Session):
    deleteOrder = db.query(database_models.Order).filter(database_models.Order.orderId==orderId).first()
    if deleteOrder:
        db.delete(deleteOrder)
        db.commit()
        return f"Order {orderId} deleted successfully"
    else:

        return f"Order {orderId} not found"