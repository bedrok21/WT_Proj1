from pydantic import BaseModel
from datetime import date, time

class User(BaseModel):
    id: int
    username: str
    email: str
    password_hash: str

class Movie(BaseModel):
    id: int
    title: str
    description: str
    release_date: date
    duration: int
    picture: str

class Movie_create(BaseModel):
    title: str
    description: str
    release_date: date
    duration: int
    picture: str

class Genre(BaseModel):
    id: int
    genre_name: str

class Genre_create(BaseModel):
    genre_name: str

class MovieGenre(BaseModel):
    id: int
    movie_id: int
    genre_id: int

class MovieGenre_create(BaseModel):
    movie_id: int
    genre_id: int

class Theatre(BaseModel):
    id: int
    theatre_name: str
    location: str
    latitude: float
    longtitude: float

class Theatre_create(BaseModel):
    theatre_name: str
    location: str
    latitude: float
    longtitude: float

class Format(BaseModel):
    id: int
    format_name: str

class Format_create(BaseModel):
    format_name: str

class Show(BaseModel):
    id: int
    theatre_id: int
    movie_id: int
    hall: int
    date: date
    time: time
    format_id: int
    price: float

class Show_create(BaseModel):
    theatre_id: int
    movie_id: int
    hall: int
    date: date
    time: time
    format_id: int
    price: float

class Status(BaseModel):
    id: int
    status_name: str

class Status_create(BaseModel):
    status_name: str

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

class UserLogin(BaseModel):
    email: str
    password: str

class UserCreate(BaseModel):
    email: str
    password: str
