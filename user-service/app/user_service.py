# from sqlalchemy.orm import Session
# from app import models, schemas, producer

# def create_user_service(db: Session, user: schemas.UserCreate) -> models.User:
#     db_user = models.User(**user.dict())
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     producer.send_user_created_event(db_user.id, user.dict())
#     return db_user

# def get_all_users_service(db: Session):
#     return db.query(models.User).all()

# def update_user_service(db: Session, user_id: int, user: schemas.UserUpdate):
#     db_user = db.query(models.User).filter(models.User.id == user_id).first()
#     if not db_user:
#         return None
#     for key, value in user.dict(exclude_unset=True).items():
#         setattr(db_user, key, value)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def delete_user_service(db: Session, user_id: int):
#     db_user = db.query(models.User).filter(models.User.id == user_id).first()
#     if not db_user:
#         return False
#     db.delete(db_user)
#     db.commit()
#     return True
