from typing import List
from fastapi import HTTPException, status, Depends, APIRouter
from .. import database
from sqlalchemy.orm import Session
from .. import models
from ..schema import VoteRow, Vote
from .. import oauth2

router = APIRouter(prefix="/votes", tags=["Votes"])


@router.get("/get_votes", response_model=List[VoteRow])
def get_votes(db: Session = Depends(database.get_db), limit: int = 10):
    limit = min(100, limit)
    query = db.query(models.Vote)
    votes = query.limit(limit).all()
    if not votes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No Votes Found"
        )
    return votes


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote_post(
    vote: Vote,
    db: Session = Depends(database.get_db),
    user: models.User = Depends(oauth2.get_current_user),
):
    post = db.query(models.Post).filter(models.Post.uuid == vote.post_uid)
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="this post is not found."
        )

    query = db.query(models.Vote).filter(
        models.Vote.post_uid == vote.post_uid, models.Vote.user_uid == user.uuid
    )

    found_vote = query.first()
    if vote.dir:
        if found_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"{user.username} has already voted to this {vote.post_uid}",
            )
        new_vote = models.Vote(post_uid=vote.post_uid, user_uid=user.uuid)
        db.add(new_vote)
        db.commit()
        return {
            "message": f"successfully add the vote to post {vote.post_uid} by {user.username}"
        }
    else:
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"no vote found by the user {user.username} on post {vote.post_uid}, can not remove the vote",
            )
        query.delete(synchronize_session=False)
        db.commit()
        return {"message": f"vote been removed successfully from post {vote.post_uid}"}
