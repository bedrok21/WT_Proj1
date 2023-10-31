from fastapi import APIRouter, Depends, HTTPException, Form, status
from fastapi_cache.decorator import cache
from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_async_session
from . import crud, schemas
import asyncio
router = APIRouter(prefix="/api")


@router.get("/movies", response_model=list[schemas.Movie])
@cache(expire=60)
async def get_movies(session: AsyncSession = Depends(get_async_session)):
    return await crud.get_movies(session)

@router.get("/movie/{movie_id}", response_model=schemas.Movie)
@cache(expire=60)
async def get_movie(movie_id: int, session: AsyncSession = Depends(get_async_session)):
    return await crud.get_movie_by_id(session, movie_id)

@router.post("/movie", status_code=status.HTTP_201_CREATED)
async def create_movie(new_movie: schemas.Movie_create, session: AsyncSession = Depends(get_async_session)):
    await crud.create_movie(session, new_movie)

@router.put("/movie/{movie_id}")
async def update_movie(movie_id:int, updated_movie: schemas.Movie_create, session: AsyncSession = Depends(get_async_session)):
    await crud.update_movie_details(session, movie_id, updated_movie)

@router.delete("/movie/{movie_id}")
async def delete_movie(movie_id: int, session: AsyncSession = Depends(get_async_session)):
    await crud.delete_movie(session, movie_id)

###################################################################################

@router.get("/theatres")
@cache(expire=60)
async def get_theatres(session: AsyncSession = Depends(get_async_session)):
    return await crud.get_theatres(session)

@router.get("/theatre/{theatre_id}", response_model=schemas.Theatre)
@cache(expire=60)
async def get_theatre(theatre_id: int, session: AsyncSession = Depends(get_async_session)):
    return await crud.get_theatre_by_id(session, theatre_id)

@router.post("/theatre", status_code=status.HTTP_201_CREATED)
async def create_theatre(new_theatre: schemas.Theatre_create, session: AsyncSession = Depends(get_async_session)):
    await crud.create_theatre(session, new_theatre)

@router.put("/theatre/{theatre_id}")
async def create_theatre(theatre_id:int, new_theatre: schemas.Theatre_create, session: AsyncSession = Depends(get_async_session)):
    await crud.update_theatre_details(session, theatre_id, new_theatre)

@router.delete("/theatre/{theatre_id}")
async def delete_theatre(theatre_id: int, session: AsyncSession = Depends(get_async_session)):
    await crud.delete_theatre(session, theatre_id)

###################################################################################

@router.get("/shows")
@cache(expire=60)
async def get_shows(session: AsyncSession = Depends(get_async_session)):
    return await crud.get_shows(session)

@router.get("/show/{show_id}")
@cache(expire=60)
async def get_show(show_id: int, session: AsyncSession = Depends(get_async_session)):
    return await crud.get_show_by_id(session, show_id)

@router.post("/show", status_code=status.HTTP_201_CREATED)
async def create_show(new_show: schemas.Show_create, session: AsyncSession = Depends(get_async_session)):
    await crud.create_show(session, new_show)

@router.put("/show/{show_id}")
async def create_theatre(show_id:int, new_show: schemas.Show_create, session: AsyncSession = Depends(get_async_session)):
    await crud.update_show_details(session, show_id, new_show)

@router.delete("/show/{show_id}")
async def create_show(show_id: int, session: AsyncSession = Depends(get_async_session)):
    await crud.delete_show(session, show_id)

###############################################################################################

@router.get("/statuses")
@cache(expire=60)
async def get_statuses(session: AsyncSession = Depends(get_async_session)):
    return await crud.get_statuses(session)

@router.post("/status", status_code=status.HTTP_201_CREATED)
async def create_status(new_status: schemas.Status_create, session: AsyncSession = Depends(get_async_session)):
    await crud.create_status(session, new_status)

@router.delete("/status/{status_id}")
async def delete_status(status_id: int, session: AsyncSession = Depends(get_async_session)):
    await crud.delete_status(session, status_id)

############################################################################

@router.get("/formats")
@cache(expire=60)
async def get_formats(session: AsyncSession = Depends(get_async_session)):
    return await crud.get_formats(session)

@router.post("/format", status_code=status.HTTP_201_CREATED)
async def create_format(new_format: schemas.Format_create, session: AsyncSession = Depends(get_async_session)):
    await crud.create_format(session, new_format)

@router.delete("/format/{format_id}")
async def delete_format(format_id: int, session: AsyncSession = Depends(get_async_session)):
    await crud.delete_format(session, format_id)

##############################################################################

@router.get("/genres")
@cache(expire=60)
async def get_genres(session: AsyncSession = Depends(get_async_session)):
    return await crud.get_genres(session)

@router.post("/genre", status_code=status.HTTP_201_CREATED)
async def create_genre(new_genre: schemas.Genre_create, session: AsyncSession = Depends(get_async_session)):
    await crud.create_genre(session, new_genre)

@router.delete("/genre/{genre_id}")
async def delete_genre(genre_id:int, session: AsyncSession = Depends(get_async_session)):
    await crud.delete_genre(session, genre_id)

################################################################################

@router.get("/movie_genres")
@cache(expire=60)
async def get_movie_genres(session: AsyncSession = Depends(get_async_session)):
    return await crud.get_movie_genres(session)

@router.post("/movie_genre", status_code=status.HTTP_201_CREATED)
async def create_movie_genre(new_movie_genre: schemas.MovieGenre_create, session: AsyncSession = Depends(get_async_session)):
    await crud.create_movie_genre(session, new_movie_genre)

@router.delete("/movie_genre/{movie_genre_id}")
async def delete_movie_genre(movie_genre_id:int, session: AsyncSession = Depends(get_async_session)):
    await crud.delete_movie_genre(session, movie_genre_id)
