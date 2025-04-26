from pydantic import BaseModel, EmailStr, Field
from typing import Annotated, Optional
from sqlalchemy import Column, Integer, String
from .db import Base

# Regex to allow digits only, 10-15 digits (adjust as needed)
PhoneStr = Annotated[str, Field(pattern=r'^\+?[0-9]{10,15}$')]

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    phonenumber = Column(String)
    
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    phone: PhoneStr

class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[PhoneStr]

class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    phone: PhoneStr

# Add your event model
class UserEvent(BaseModel):
    user_id: int
    event_type: str
    timestamp: str
    details: dict
