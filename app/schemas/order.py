
from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal


class OrderItemCreate(BaseModel):
    menu_item_id: int = Field(gt=0)
    quantity: int = Field(gt=0)


class OrderCreate(BaseModel):
    restaurant_id: int = Field(gt=0)
    items: list[OrderItemCreate] = Field(min_length=1)

class OrderItemResponse(BaseModel):
    id: int
    menu_item_id: int
    quantity: int
    unit_price: Decimal

    model_config = ConfigDict(from_attributes=True)
    
class OrderResponse(BaseModel):
    id: int
    customer_id: int
    restaurant_id: int
    total_amount: Decimal
    status: str
    items: list[OrderItemResponse]

    model_config = ConfigDict(from_attributes=True)
