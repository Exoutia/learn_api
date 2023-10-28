from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models
from ..database import get_db
from ..schema import CreateUser, User
from ..utils import hash_password

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[User])
def get_users(db: Session = Depends(get_db)) -> List[User]:
    my_users = db.query(models.User).all()
    print(my_users)
    return my_users


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(user: CreateUser, db: Session = Depends(get_db)) -> User:
    username = user.username
    email = user.email
    password = user.password
    hashed_password = hash_password(password)
    new_user = models.User(username=username, email=email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)) -> User:
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id {user_id} not found",
        )
    else:
        return user
