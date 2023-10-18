from fastapi import FastAPI, status, HTTPException, Depends
from . import models
from .schema import Post, CreatePost, UpdatePost
from .database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
import bcrypt

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



