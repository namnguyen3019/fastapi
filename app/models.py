from tkinter.tix import Tree

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, unique=True,
                index=True, autoincrement=True)
    email = Column(String, primary_key=True, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    posts = relationship(
        'PostBase', back_populates="owner", cascade="all, delete", passive_deletes=True)
    phone_number = Column(String)


class PostBase(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, unique=True,
                index=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    owner = relationship("User", back_populates="posts")


class Post(PostBase):
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))


class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey(
        'users.id', ondelete='CASCADE'), primary_key=True)
    post_id = Column(Integer, ForeignKey(
        'posts.id', ondelete='CASCADE'), primary_key=True)
