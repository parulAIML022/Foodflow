from sqlalchemy.orm import Session
from app.repositories.restaurant_repository import create_restaurant
from app.repositories.restaurant_repository import(
    create_restaurant,
    get_all_restaurants,
    get_restaurant_by_id,
    update_restaurant,
    delete_restaurant
)
def create_new_restaurant(
        db: Session,
        name: str,
        description: str | None,
        address: str
):
    restaurant = create_restaurant(
        db=db,
        name=name,
        description=description,
        address=address
    )
    return restaurant
def get_restaurants(db: Session):
    restaurants = get_all_restaurants(db)
    return restaurants
def get_restaurant(db: Session, restaurant_id: int):
    restaurant = get_restaurant_by_id(db, restaurant_id)
    return restaurant 
def update_existing_restaurant(
    db: Session,
    restaurant_id: int,
    name: str,
    description: str | None,
    address: str
):
    return update_restaurant(
        db=db,
        restaurant_id=restaurant_id,
        name=name,
        description=description,
        address=address
    )
def delete_existing_restaurant(
        db:Session,
        restaurant_id: int
):
    restaurant = delete_restaurant(
        db=db,
        restaurant_id=restaurant_id 
    )
    return restaurant