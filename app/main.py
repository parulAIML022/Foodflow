from fastapi import FastAPI
from app.api.v1.health import router as health_router
from app.api.v1.auth import router as auth_router
from app.api.v1.restaurant import router as restaurant_router
from app.api.v1 import menu
app = FastAPI(
    title="Floodflow API",
    description="Food ordering and restaurant management backend",
    version="1.0.0"
)
@app.get("/")
def root():
    return{
         "message": "Welcome to FoodFlow API"
    }
app.include_router(health_router)
app.include_router(auth_router) 
app.include_router(restaurant_router)
app.include_router(menu.router)


