import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String (250), unique=True, nullable=False)
    password = Column(String(200), nullable=False)

class Photographer(Base):
    __tablename__ = 'photographer'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String (250), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    photos_id = Column(Integer, ForeignKey('photos.id'))
    uploaded_photos = relationship ("Photos")

class Favourites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    photographer_id = Column(Integer, ForeignKey('photographer.id'))
    photographer = relationship(Photographer)
    photo_id = Column(Integer, ForeignKey('photos.id'))
    photo = relationship("Photos")

class Photos(Base):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True)
    picture = Column(String(100), nullable=False)
    price = Column(String(20), nullable=False)

class FAQ (Base):
    __tablename__ = 'faq'
    id = Column(Integer, primary_key=True)
    questions = Column(String(500), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

class Comments (Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comments = Column(String(1000), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True)
    date = Column(String(20), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    photo_id = Column(Integer, ForeignKey('photos.id'))
    photo = relationship(Photos)

class Category (Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    description = Column(String(1000), nullable=False)
    photo_id = Column(Integer, ForeignKey('photos.id'))
    photo = relationship(Photos)

class Followers(Base):
    __tablename__ = "followers"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    photographer_id = Column(Integer, ForeignKey('photographer.id'))
    photographer = relationship(Photographer)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
