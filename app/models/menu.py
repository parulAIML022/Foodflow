from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey,Boolean, Numeric
from sqlalchemy.sql import func
from app.database.database import Base

class Menu(Base):
    __tablename__ = "menu_items"
    id = Column(Integer,
                primary_key=True,
                index=True)
    restaurant_id = Column(
        Integer,
        ForeignKey("restaurants.id"), 
        nullable=False
    )
    name = Column(
        String(150),
        nullable=False 
    )
    description = Column(
        Text,
        nullable=True
    )
    price = Column(
        Numeric(10,2),
        nullable=False
    )
    category = Column( String(100),
        nullable=False)
    is_available = Column(
        Boolean,
        default=True,
        nullable=False
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )