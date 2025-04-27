from pydantic import BaseModel, EmailStr
from typing import Optional

class UserRegister(BaseModel):
    name: str
    email: str
    phone: str
    password: str

class UserCreate(BaseModel):
    name: str
    email: str
    phone: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str

    class Config:
        from_attributes  = True

class UserCreateResponse(BaseModel):
    message: str
    user: UserResponse

class UserRegisterResponse(BaseModel):
    message: str
    user: UserResponse