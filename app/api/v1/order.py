
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.order import OrderCreate, OrderResponse
from app.services.order_service import (
    create_new_order,
    get_order_details,
    get_customer_order_history,
    cancel_customer_order
)
from app.core.security import get_current_user


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("/", response_model=OrderResponse)
def place_order(
    order_data: OrderCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return create_new_order(
        db=db,
        customer_id=current_user.id,
        order_data=order_data
    )


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_order_details(
        db=db,
        order_id=order_id,
        customer_id=current_user.id
    )


@router.get("/", response_model=list[OrderResponse])
def get_my_orders(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_customer_order_history(
        db=db,
        customer_id=current_user.id
    )

@router.patch("/{order_id}/cancel",response_model=OrderResponse)
def cancel_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return cancel_customer_order(
        db=db,
        order_id=order_id,
        customer_id=current_user.id
    )