from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models
from ..database import get_db
from ..schema import CreatePost, Post, UpdatePost

from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
)


@router.get("/", response_model=List[Post])
def get_posts(
    db: Session = Depends(get_db),
    limit: int = 10,
    skip: int = 0,
    search: str | None = None,
) -> List[Post]:
    limit = min(limit, 100)
    if search:
        all_posts = (
            db.query(models.Post)
            .filter(models.Post.title.contains(search))
            .offset(skip)
            .limit(limit)
            .all()
        )
    else:
        all_posts = db.query(models.Post).offset(skip).limit(limit).all()
    if not all_posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="no posts found"
        )
    return all_posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Post)
def create_post(
    post: CreatePost,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    user_uid = user.uuid
    title = post.title
    content = post.content
    published = post.published
    new_post = models.Post(
        title=title, content=content, published=published, user_uid=user_uid
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/myPosts", response_model=List[Post])
def get_users_post(
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
    limit: int = 10,
    skip: int = 0,
    search: str | None = None,
) -> List[Post]:
    limit = min(limit, 100)
    if search:
        my_posts = (
            db.query(models.Post)
            .filter(models.Post.title.contains(search))
            .filter(models.Post.user_uid == user.uuid)
            .offset(skip)
            .limit(limit)
            .all()
        )
    else:
        my_posts = (
            db.query(models.Post)
            .filter(models.Post.user_uid == user.uuid)
            .offset(skip)
            .limit(limit)
            .all()
        )
    # print(len(my_posts))
    if not my_posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user has not posted anything yet",
        )
    return my_posts


@router.get("/{post_id}", response_model=Post)
def get_post(post_id: int, db: Session = Depends(get_db)) -> Post:
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {post_id} not found",
        )
    else:
        return post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
) -> None:
    query = db.query(models.Post).filter(models.Post.id == post_id)
    post = query.first()
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {post_id} not found",
        )
    if user.uuid != post.user_uid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"you are not allowed to delete this post: {post_id}",
        )
    else:
        # to remember to delete post wejust need query not the row.
        query.delete(synchronize_session=False)
        db.commit()
        return


@router.put("/{post_id}", status_code=status.HTTP_202_ACCEPTED, response_model=Post)
def update_post(
    post_id: int,
    post: UpdatePost,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
) -> Post:
    query = db.query(models.Post).filter(models.Post.id == post_id)
    updated_post = query.first()

    if updated_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {post_id} not found",
        )
    elif user.uuid != updated_post.user_uid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"you are not allowed to change this post: {post_id}",
        )
    else:
        query.update(post.dict(), synchronize_session=False)
        db.commit()
        updated_post = query.first()
        return updated_post
