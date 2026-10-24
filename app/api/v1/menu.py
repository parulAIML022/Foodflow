from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from app.database.database import get_db
from app.schemas.menu import MenuCreate, MenuResponse
from app.services.menu_service import(
    create_new_menu_item,
    get_menu_item_by_id,
    get_restaurant_menu,
    update_existing_menu_item,
    delete_existing_menu_item,
)
router = APIRouter(
    prefix="/menu",
    tags=["Menu"]
)

@router.post("",response_model=MenuResponse)
def create_menu(
    menu_data: MenuCreate,
    db: Session = Depends(get_db)
):
    return create_new_menu_item(db,menu_data)

@router.get(
    "/restaurant/{restaurant_id}",
    response_model=list[MenuResponse]
)
def get_menu_for_restaurant(
    restaurant_id: int,
    db: Session = Depends(get_db)
):
    return get_restaurant_menu(db,restaurant_id)

@router.get("/{menu_id}",response_model=MenuResponse)
def get_one_menu_item(
    menu_id: int,
    db: Session = Depends(get_db)
):
    return get_menu_item_by_id(db,menu_id)

@router.put("/{menu_id}",response_model=MenuResponse)
def update_menu(
    menu_id: int,
    menu_data: MenuCreate,
    db: Session = Depends(get_db)
):
    return update_existing_menu_item(
        db=db,
        menu_id=menu_id,
        menu_data=menu_data.model_dump()
    )

@router.delete("/{menu_id}")
def delete_menu(
    menu_id: int,
    db: Session = Depends(get_db)
):
    delete_existing_menu_item(db,menu_id)
    return {"message": "Menu item deleted successfully"}