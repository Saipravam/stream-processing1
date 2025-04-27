# from fastapi import FastAPI, Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from sqlalchemy.orm import Session
# from app import models, schemas, database, kafka_producer, auth  # import your new auth
# from app.database import SessionLocal, engine

# app = FastAPI()

# models.Base.metadata.create_all(bind=engine)
# database.init_db()

# # OAuth2
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # LOGIN Endpoint 
# @app.post("/login")
# def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.email == form_data.username).first()
#     if not user:
#         raise HTTPException(status_code=400, detail="Incorrect email or password")

#     if not auth.verify_password(form_data.password, user.hashed_password):
#         raise HTTPException(status_code=400, detail="Incorrect email or password")

#     access_token = auth.create_access_token(data={"sub": user.email})
#     return {"access_token": access_token, "token_type": "bearer"}

# # PROTECTED Endpoint 
# @app.get("/protected-route")
# def protected_route(token: str = Depends(oauth2_scheme)):
#     payload = auth.decode_access_token(token)
#     if not payload:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
#     return {"message": "You are authenticated!", "user": payload.get("sub")}
