from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import models
from .database import engine, get_db
from .schema import CreatePost, CreateUser, Post, UpdatePost, User
from .utils import hash_password

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
def say_hello():
    return {"message": "post app"}


@app.get("/posts")
def get_posts(db: Session = Depends(get_db), response_model=List[Post]):
    my_posts = db.query(models.Post).all()
    return my_posts


@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=Post)
def create_post(post: CreatePost, db: Session = Depends(get_db)) -> Post:
    title = post.title
    content = post.content
    published = post.published
    new_post = models.Post(title=title, content=content, published=published)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@app.get("/posts/{post_id}", response_model=Post)
def get_post(post_id: int, db: Session = Depends(get_db)) -> Post:
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {post_id} not found",
        )
    else:
        return post


@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)) -> None:
    query = db.query(models.Post).filter(models.Post.id == post_id)
    if query.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {post_id} not found",
        )
    else:
        # to remember to delete post wejust need query not the row.
        query.delete(synchronize_session=False)
        db.commit()
        return


@app.put("/posts/{post_id}", status_code=status.HTTP_202_ACCEPTED, response_model=Post)
def update_post(post_id: int, post: UpdatePost, db: Session = Depends(get_db)) -> Post:
    query = db.query(models.Post).filter(models.Post.id == post_id)
    updated_post = query.first()

    if updated_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {post_id} not found",
        )
    else:
        query.update(post.dict(), synchronize_session=False)
        db.commit()
        updated_post = query.first()
        return updated_post


@app.get("/users", response_model=List[User])
def get_users(db: Session = Depends(get_db)):
    my_users = db.query(models.User).all()
    print(my_users)
    return my_users


@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    username = user.username
    email = user.email
    password = user.password
    salt, hashed_password = hash_password(password)
    new_user = models.User(
        username=username, email=email, salt=salt, password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id {user_id} not found",
        )
    else:
        return user
