from decimal import Decimal
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.order import Order, OrderItem
from app.models.menu import Menu 
from app.schemas.order import OrderCreate
from app.repositories.order_repository import (
    create_order,
    get_order_by_id,
    get_orders_by_customer,
    update_order_status
)
def create_new_order(
        db:Session,
        customer_id: int,
        order_data: OrderCreate
) -> Order:
    order_items = []
    total_amount = Decimal("0.00")
    for item in order_data.items:
        menu_item = (
            db.query(Menu)
            .filter(Menu.id == item.menu_item_id)
            .first()
        )
        if not menu_item:
            raise HTTPException(
                    status_code=400,
                    detail=f"Menu item {item.menu_item_id} is unavailable"
                )
        if menu_item.restaurant_id != order_data.restaurant_id:
            raise HTTPException(
                    status_code=400,
                    detail="All menu items must belong to the selected restaurant"
                )
        unit_price = Decimal(str(menu_item.price))
        total_amount += unit_price * item.quantity
        order_items.append(
                OrderItem(
                    menu_item_id=menu_item.id,
                    quantity=item.quantity,
                    unit_price=unit_price
                    )
                )
        new_order = Order(
                customer_id=customer_id,
                restaurant_id=order_data.restaurant_id,
                total_amount=total_amount,
                status="pending",
                items=order_items 
                )
        return create_order(db,new_order)
def get_order_details(
                db: Session,
                order_id: int,
                customer_id: int 
                ) -> Order:
                order = get_order_by_id(db, order_id)
                if not order:
                   raise HTTPException(status_code=404,detail="Order not found")
                if order.customer_id != customer_id:
                   raise HTTPException(status_code=403, detail="Access denied")
                return order 
def get_customer_order_history(
                db: Session,
                customer_id: int
) -> list[Order]:
    return get_orders_by_customer(db, customer_id)
def cancel_customer_order(
        db:Session,
        order_id: int,
        customer_id: int
) -> Order:
     order = get_order_by_id(db,order_id)
     if not order:
          raise HTTPException(
               status_code=404,
               detail="Order not found"
          )
     if order.customer_id != customer_id:
          raise HTTPException(
               status_code=403,
               detail="You cannot cancel someone else's order"
          )
     if order.status != "pending":
          raise HTTPException(
               status_code=400,
               detail="Only pending orders can be cancelled"
          )
     return update_order_status(
          db=db,
          order=order,
          status="cancelled"
     )