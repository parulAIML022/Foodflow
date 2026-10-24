from sqlalchemy.orm import Session
from app.models.menu import Menu
from app.schemas.menu import MenuCreate
def create_menu_item(db:Session, menu_data: MenuCreate):
    db_menu = Menu(**menu_data.model_dump()) #conv validated pyd data into keyw args for sqlalchemy model
    db.add(db_menu) #stages the new obj in sqlalchemy session
    db.commit() #saves the transaction to mysql
    db.refresh(db_menu) #retrieves db-gen values,such as new id
    return db_menu 

def get_menu_item(db:Session, menu_id: int):
    return db.query(Menu).filter(Menu.id == menu_id).first()
def get_menu_by_restaurant(db:Session, restaurant_id: int):
    return db.query(Menu).filter(
        Menu.restaurant_id == restaurant_id
    ).all()
def update_menu_item(db:Session,db_menu:Menu, menu_data:dict):
    for key,value in menu_data.items():
        setattr(db_menu,key,value)
    db.commit()
    db.refresh(db_menu)
    return db_menu
def delete_menu_item(db:Session, db_menu:Menu):
    db.delete(db_menu)
    db.commit()