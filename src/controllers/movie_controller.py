from fastapi import APIRouter, Depends, HTTPException, Form, Query
from starlette.requests import Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date, time
from src.database import get_async_session
from src.schemas import Movie_create, Movie
import src.crud
from .utils import get_page_link

router = APIRouter(prefix="", include_in_schema=False)
templates = Jinja2Templates(directory="src/templates/")


@router.get("/movie")
async def get_movies(request: Request, session: AsyncSession = Depends(get_async_session),
                     skip: int = Query(0, title="Skip"),
                 limit: int = Query(10, title="Limit")):
    movies = (await src.crud.get_movies(session, limit=limit, skip=skip))
    next_link = ''
    prev_link = ''
    if limit == len(movies):
        new_skip_next = skip + limit
        next_link = get_page_link(new_skip_next, limit, 'movie')
    if skip > 0:
        new_skip_prev = skip - limit
        if new_skip_prev < 0: new_skip_prev = 0
        prev_link = get_page_link(new_skip_prev, limit, 'movie')
    return templates.TemplateResponse("movie/index.html", {"request": request, "movies": movies, "next_link": next_link, "prev_link":prev_link})

@router.get("/movie/{movie_id}")
async def movie_details(movie_id: int, request: Request, session: AsyncSession = Depends(get_async_session)):
    movie = await src.crud.get_movie_by_id(session, movie_id)
    shows = await src.crud.get_shows_by_movie_id(session, movie_id)
    return templates.TemplateResponse("movie/details.html", {"request": request, "shows":shows,  "movie": movie})


@router.get("/movie/{movie_id}/delete")
async def movie_delete(movie_id: int, request: Request, session: AsyncSession = Depends(get_async_session)):
    return templates.TemplateResponse("movie/delete.html", {"request": request, "movie": await src.crud.get_movie_by_id(session, movie_id)})

@router.post("/movie/{movie_id}/delete")
async def movie_delete_dubmit(movie_id: int, request: Request, session: AsyncSession = Depends(get_async_session)):
    await src.crud.delete_movie(session, movie_id)
    return RedirectResponse("/movie", status_code=303)


@router.get("/movie/{movie_id}/edit")
async def edit_movie(request: Request, movie_id: int, session: AsyncSession = Depends(get_async_session)):
    movie = await src.crud.get_movie_by_id(session, movie_id)

    if movie is not None:
        return templates.TemplateResponse("movie/edit.html", {"request": request, "movie": movie})
    else:
        return {"message": "Movie not found"}

@router.post("/movie/{movie_id}/edit")
async def update_movie(request: Request,  movie_id: int, title: str = Form(...), description: str = Form(...),
                       release_date: date = Form(...), duration: int = Form(...), picture: str = Form(...), session: AsyncSession = Depends(get_async_session)):
    updated_movie = Movie_create(title=title, description=description,release_date=release_date,duration=duration,picture=picture)
    movie = await src.crud.update_movie_details(session, movie_id, updated_movie)
    if movie is not None:
        return templates.TemplateResponse("movie/edit.html", {"request": request, "movie": movie})
    else:
        return {"message": "Movie not found"}


@router.get("/movie-create")
async def add_movie(request: Request):
    return templates.TemplateResponse("movie/create.html", {"request": request})

@router.post("/movie-create")
async def submit_add_movie(title: str = Form(...),description: str = Form(...), release_date: date = Form(...),
                           duration: int = Form(...), picture: str = Form(...), session: AsyncSession = Depends(get_async_session)):
    new_movie = Movie_create(title=title, description=description, release_date=release_date, duration=duration, picture=picture)
    await src.crud.create_movie(session, new_movie)
    return RedirectResponse("/movie", status_code=303)
