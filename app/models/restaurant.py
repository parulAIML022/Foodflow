from sqlalchemy import Column,Integer,String,Text,DateTime
from sqlalchemy.sql import func
from app.database.database import Base
class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(
        Integer,
        primary_key=True,
        index=True 
    )
    name= Column(
        String(150),
        nullable=False
    )
    description= Column(
        Text,
        nullable=True
    )
    address = Column(
        String(255),
        nullable=False
    )
    created_at = Column(
        DateTime,
        server_default=func.now()
    )