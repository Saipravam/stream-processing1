from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    phonenumber: str

class UserUpdate(BaseModel):
    username: str = None
    email: str = None
    phonenumber: str = None

class UserOut(UserCreate):
    id: int

    class Config:
        orm_mode = True
