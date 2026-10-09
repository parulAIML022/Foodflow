from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user import UserCreate,UserLogin, UserResponse
from app.services.auth_service import register_user, login_user


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    try:
        user = register_user(
            db=db,
            name=user_data.name,
            email=user_data.email,
            password=user_data.password
        )

        return user

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
@router.post("/login")
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):
    try:
        token = login_user(
            db=db,
            email= user_data.email,
            password= user_data.password
        )
        return{
            "access_token": token,
            "token_type": "bearer"
        }
    except ValueError as e:
        raise HTTPException(
            status_code= 401,
            detail = str(e)
        )