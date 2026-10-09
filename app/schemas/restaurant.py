from pydantic import BaseModel, Field
class RestaurantCreate(BaseModel):
    name: str = Field(min_length=2, max_length=150)
    description: str | None = None
    address: str = Field(min_length=5, max_length=255)
class RestaurantUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=150)
    description: str | None = None
    address: str = Field(min_length=5, max_length=255)
class RestaurantResponse(BaseModel):
    id: int
    name: str
    description: str | None
    address: str
    model_config= {
        "from_attributes": True
    }
