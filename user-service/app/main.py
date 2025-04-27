from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app import models, schemas, database,kafka_producer
from app.database import SessionLocal, engine
from app import auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Initialize DB
database.init_db()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Register user (updated)
@app.post("/register", response_model=schemas.UserOut)
def register_user(user: schemas.UserRegister, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered.")

    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(
        name=user.name,
        email=user.email,
        phone=user.phone,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    kafka_producer.publish_user_registered_event(db_user)
    return db_user

# Create User
@app.post("/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered.")

    db_user = models.User(
        name=user.name, 
        email=user.email, 
        phone=user.phone,
        )
    db.add(db_user)
    try:
       db.commit()
       db.refresh(db_user)
    except IntegrityError:
        db.rollback()
    kafka_producer.publish_user_created_event(db_user)
    return db_user

# Get All Users
@app.get("/users", response_model=list[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    kafka_producer.publish_users_listed_event()
    return users

# Update User
@app.put("/users/{user_id}", response_model=schemas.UserOut)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    for var, value in vars(user).items():
        if value is not None:
            setattr(db_user, var, value)

    db.commit()
    db.refresh(db_user)
    kafka_producer.publish_user_updated_event(db_user)
    return db_user

# Delete User
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    kafka_producer.publish_user_deleted_event(user_id)
    return {"message": "User deleted successfully"}
