from pydantic import BaseModel
from datetime import date, time

class User(BaseModel):
    id: int
    username: str
    email: str
    password_hash: str


class Movie_create(BaseModel):
    title: str
    description: str
    release_date: date
    duration: int
    picture: str

class Movie(Movie_create):
    id: int


class Genre_create(BaseModel):
    genre_name: str

class Genre(Genre_create):
    id: int


class MovieGenre_create(BaseModel):
    movie_id: int
    genre_id: int

class MovieGenre(MovieGenre_create):
    id: int


class Theatre_create(BaseModel):
    theatre_name: str
    location: str
    latitude: float
    longtitude: float

class Theatre(Theatre_create):
    id: int


class Format_create(BaseModel):
    format_name: str

class Format(Format_create):
    id: int


class Show_create(BaseModel):
    theatre_id: int
    movie_id: int
    hall: int
    date: date
    time: time
    format_id: int
    price: float

class Show(Show_create):
    id: int


class Status_create(BaseModel):
    status_name: str

class Status(Status_create):
    id: int


class Seat(BaseModel):
    id: int
    show_id: int
    raw: int
    seat: int
    status_id: int


class UserRead(BaseModel):
    id: int
    email: str
    is_superuser: bool = False

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(UserCreate):
    pass
