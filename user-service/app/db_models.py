from sqlalchemy import Column, Integer, String
from app.database import Base

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phonenumber = Column(String, nullable=True)
