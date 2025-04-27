from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.kafka_producer import init_kafka_producer
from fastapi import APIRouter
from app import schemas,crud
from app.database import SessionLocal

router = APIRouter()

@router.post("/publish")
def publish_message(data: schemas):
    producer = init_kafka_producer()
    producer.send('user-event', b'event-published')
    producer.flush()
    return {"message": "sent"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users", response_model=schemas.UserCreateResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    return {
        "message": "User created successfully",
        "user": db_user
    }

@router.post("/users", response_model=schemas.UserRegisterResponse)
def create_user(user: schemas.UserRegister, db: Session = Depends(get_db)):
    db_user = crud.register_user(db, user)
    return {
        "message": "User registered successfully",
        "user": db_user
    }
