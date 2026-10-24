'''this service handles business logic b/w router and repo. 
it checks whether the restaurant exists before creating a menu 
item'''
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.restaurant import Restaurant
from app.schemas.menu import MenuCreate
from app.repositories.menu_repository import ( create_menu_item,
                                              get_menu_item,
                                              get_menu_by_restaurant,
                                              update_menu_item,
                                              delete_menu_item  )

def create_new_menu_item(db:Session, menu_data: MenuCreate):
    restaurant = db.query(Restaurant).filter(
        Restaurant.id == menu_data.restaurant_id
    ).first()
    if not restaurant:
        raise HTTPException(
            status_code=404,
            detail="Restaurant not found",
        )
    return create_menu_item(db,menu_data)
def get_menu_item_by_id(db:Session,menu_id:int):
    menu = get_menu_item(db,menu_id)
    if not menu:
        raise HTTPException(status_code=404,detail="Menu item not found")
    return menu
def get_restaurant_menu(db:Session,restaurant_id:int):
    restaurant = db.query(Restaurant).filter(
        Restaurant.id == restaurant_id
    ).first()
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return get_menu_by_restaurant(db,restaurant_id)
def update_existing_menu_item(
    db: Session, menu_id: int, menu_data: dict
):
    menu = get_menu_item_by_id(db, menu_id)

    if "restaurant_id" in menu_data:
        restaurant = db.query(Restaurant).filter(
            Restaurant.id == menu_data["restaurant_id"]
        ).first()

        if not restaurant:
            raise HTTPException(status_code=404, detail="Restaurant not found")

    return update_menu_item(db, menu, menu_data)


def delete_existing_menu_item(db: Session, menu_id: int):
    menu = get_menu_item_by_id(db, menu_id)
    delete_menu_item(db, menu)
'''we raise a 404 error when the requested menu item doesn't exist.
the service handles this business condition so the router doesn't need
to repeat the same validation logic.'''