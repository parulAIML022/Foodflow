
from sqlalchemy.orm import Session
from app.models.order import Order, OrderItem


def create_order(db: Session, order: Order) -> Order:
    try:
        db.add(order)
        db.commit()
        db.refresh(order)
        return order
    except Exception:
        db.rollback()
        raise



def get_order_by_id(db: Session, order_id: int) -> Order | None:
    return db.query(Order).filter(Order.id == order_id).first()


def get_orders_by_customer(db: Session, customer_id: int) -> list[Order]:
    return (
        db.query(Order)
        .filter(Order.customer_id == customer_id)
        .order_by(Order.created_at.desc())
        .all()
    )


def update_order_status(db: Session, order: Order, status: str) -> Order:
    order.status = status
    db.commit()
    db.refresh(order)
    return order
