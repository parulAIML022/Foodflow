from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal 

class MenuCreate(BaseModel):
    restaurant_id: int = Field(gt=0)
    name: str = Field(min_length=2, max_length=150)
    description: str | None = None 
    price: Decimal = Field(gt=0,max_digits=10,decimal_places=2)
    category: str = Field(min_length=2, max_length=100)
    is_available: bool = True 

class MenuResponse(BaseModel):
    id: int
    restaurant_id: int
    name: str
    description: str | None
    price: Decimal 
    category: str
    is_available: bool 

    model_config = ConfigDict(from_attributes=True) 