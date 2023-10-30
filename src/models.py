from sqlalchemy import Integer, Time, ForeignKey, Column, Table, String, Date, Float
from datetime import datetime
from sqlalchemy import (JSON, TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, Table)
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
metadata = MetaData()
Base = declarative_base()
movie = Table(
    "movie",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(250), nullable=False),
    Column("description", String(2000), nullable=False),
    Column("release_date", Date, nullable=False),
    Column("duration", Integer, nullable=False),
    Column("picture", String(500), nullable=True),
)

genre = Table(
    "genre",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("genre_name", String(30), nullable=False),
)

movie_genre = Table(
    "movie_genre",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("movie_id", Integer, nullable=False),
    Column("genre_id", Integer, nullable=False),
)
theatre = Table(
    "theatre",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("theatre_name", String(250), nullable=False),
    Column("location", String(500), nullable=False),
    Column("latitude", Float, nullable=False),
    Column("longtitude", Float, nullable=False)
)

format = Table(
    "format",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("format_name", String(10), nullable=False),
)

show = Table(
    "show",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("theatre_id", Integer, ForeignKey("theatre.id")),
    Column("movie_id", Integer, ForeignKey("movie.id")),
    Column("hall", Integer, nullable=False),
    Column("date", Date, nullable=False),
    Column("time", Time, nullable=False),
    Column("format_id", Integer, ForeignKey("format.id")),
    Column("price", Float, nullable=False),
)

status = Table(
    "status",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("status_name", String(20), nullable=False),
)

seat = Table(
    "seat",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("show_id", Integer, ForeignKey("show.id")),
    Column("raw", Integer, nullable=False),
    Column("seat", Integer, nullable=False),
    Column("status_id", Integer, ForeignKey("status.id"))
)

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email",String, nullable=False),
    Column("password",String(length=1024), nullable=False),
    Column("is_superuser",Boolean, default=False, nullable=False),
)
