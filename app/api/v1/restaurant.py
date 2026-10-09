from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.restaurant import RestaurantCreate, RestaurantResponse, RestaurantUpdate
from app.services.restaurant_service import (create_new_restaurant,
                                             get_restaurants,
                                             get_restaurant,
                                             update_existing_restaurant,
                                             delete_existing_restaurant)
router = APIRouter(
    prefix="/restaurants",
    tags=["Restaurants"]
)
@router.post(
    "",
    response_model=RestaurantResponse
)
def create_restaurant(
    restaurant_data: RestaurantCreate,
    db: Session = Depends(get_db)
):
    restaurant = create_new_restaurant(
        db=db,
        name=restaurant_data.name,
        description=restaurant_data.description,
        address=restaurant_data.address
    )

    return restaurant
@router.get(
    "",
    response_model=list[RestaurantResponse]
)
def get_all_restaurants(
    db: Session = Depends(get_db)
):
    restaurants = get_restaurants(db)
    return restaurants
@router.get(
    "/{restaurant_id}",
    response_model=RestaurantResponse
)
def get_one_restaurant(
    restaurant_id: int,
    db: Session = Depends(get_db)
):
    restaurant = get_restaurant(
        db,
        restaurant_id 
    )
    if restaurant is None:
        raise HTTPException(
            status_code=404,
            detail="Restaurant not found"
        )
    return restaurant 
@router.put(
    "/{restaurant_id}",
    response_model=RestaurantResponse
)
def update_restaurant(
    restaurant_id: int,
    restaurant_data: RestaurantUpdate,
    db: Session = Depends(get_db)
):
    restaurant = update_existing_restaurant(
        db=db,
        restaurant_id=restaurant_id,
        name=restaurant_data.name,
        description=restaurant_data.description,
        address=restaurant_data.address
    )

    if restaurant is None:
        raise HTTPException(
            status_code=404,
            detail="Restaurant not found"
        )

    return restaurant
@router.delete("/{restaurant_id}")
def delete_restaurant(
    restaurant_id: int,
    db: Session = Depends(get_db)
):
    restaurant = delete_existing_restaurant(
        db=db,
        restaurant_id=restaurant_id
    )

    if restaurant is None:
        raise HTTPException(
            status_code=404,
            detail="Restaurant not found"
        )

    return {
        "message": "Restaurant deleted successfully"
    }