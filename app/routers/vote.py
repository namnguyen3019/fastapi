from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, oauth2, schemas
from ..database import get_db

router = APIRouter(prefix='/vote')


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(get_db), cur_user=Depends(oauth2.get_current_user)):

    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id, models.Vote.user_id == cur_user.id)

    vote_found = vote_query.first()

    if not vote_found:
        post = db.query(models.Post).filter(
            models.Post.id == vote.post_id).first()

        if not post:
            return "post not found"
        else:
            if vote.dir == 1:
                new_vote = models.Vote(
                    post_id=vote.post_id, user_id=cur_user.id)
                db.add(new_vote)
                db.commit()
                return "Add a new vote"
            else:
                return "Not vote yet"
    else:
        if vote.dir == 1:
            return "Already voted"
        else:
            db.delete(vote_found)
            db.commit()
            return "Delete a vote"
