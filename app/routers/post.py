from distutils.debug import DEBUG
from itertools import count
from typing import List, Optional

from app import oauth2
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/posts",
    tags=['posts']
)


@router.get("/", response_model=List[schemas.PostRes])
def get_posts(db: Session = Depends(get_db), current_user: schemas.UserResponse = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search_text: Optional[str] = ""):

    posts = db.query(models.Post, func.count(models.Vote.user_id).label("votes")).outerjoin(
        models.Vote, models.Post.id == models.Vote.post_id).group_by(models.Post.id).filter(
        models.Post.owner_id == current_user.id).offset(skip).limit(limit).all()

    return posts


@router.get("/{id}", response_model=schemas.PostRes)
def get_post(id: int, db: Session = Depends(get_db), current_user=Depends(oauth2.get_current_user)):
    post = db.query(models.Post, func.count(models.Vote.user_id).label("votes")).outerjoin(
        models.Vote, models.Post.id == models.Vote.post_id).group_by(models.Post.id).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

    return post


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user=Depends(oauth2.get_current_user)):
    new_post = models.Post(
        owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    return None


@router.put("/{id}", status_code=status.HTTP_200_OK)
def update_post(id: int, updatedPost: schemas.PostCreate):
    return None
