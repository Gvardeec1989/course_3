from sqlalchemy import Column, String, Integer, Float, ForeignKey

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'
    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'
    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movies'
    title = Column(String(255))
    description = Column(String(255))
    trailer = Column(String(255))
    year = Column(Integer)
    rating = Column(Float)
    genre_id = Column(Integer, ForeignKey(f'{Genre.__tablename__}.id'))
    director_id = Column(Integer, ForeignKey(f'{Director.__tablename__}.id'))


class User(models.Base):
    __tablename__ = 'Users'
    email = Column(String(255))
    password = Column(String(255))
    name = Column(String(255))
    surname = Column(String(255))
    favourite_genre = Column(Integer, ForeignKey(f'{Genre.__tablename__}.id'))
