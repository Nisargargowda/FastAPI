from fastapi import APIRouter, Depends, status, HTTPException
import models, schemas
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(
    prefix="/users",
    tags = ["Users"]

)


@router.get("/users", response_model=list[schemas.User])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.get("/users/{username}", response_model=schemas.User)
def get_user(username: str, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == username).first()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return db_user

@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    db_user = models.User(username=user.username, name=user.name, age=user.age, gender=user.gender)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
