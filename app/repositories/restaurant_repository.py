from sqlalchemy.orm import Session
from app.models.restaurant import Restaurant
def create_restaurant(
    db: Session,
    name: str,
    description: str | None,
    address: str 
):
    restaurant = Restaurant(
        name=name,
        description=description,
        address=address
    )
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return restaurant 
def get_all_restaurants(db: Session):
    return db.query(Restaurant).all()
def get_restaurant_by_id(db: Session, restaurant_id: int):
    return(
        db.query(Restaurant)
        .filter(Restaurant.id == restaurant_id)
        .first()
    )
def update_restaurant(
    db: Session,
    restaurant_id: int,
    name: str,
    description: str | None,
    address: str
):
    restaurant = (
        db.query(Restaurant)
        .filter(Restaurant.id == restaurant_id)
        .first()
    )

    if restaurant is None:
        return None

    restaurant.name = name
    restaurant.description = description
    restaurant.address = address

    db.commit()
    db.refresh(restaurant)

    return restaurant
def delete_restaurant(
    db: Session,
    restaurant_id: int
):
    restaurant = (
        db.query(Restaurant)
        .filter(Restaurant.id == restaurant_id)
        .first()
    )

    if restaurant is None:
        return None

    db.delete(restaurant)
    db.commit()

    return restaurant