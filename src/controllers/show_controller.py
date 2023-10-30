from fastapi import APIRouter, Depends, HTTPException, Request, Form, Query
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date, time
from src.database import get_async_session
from src.schemas import Show_create, Show
import src.crud
from .utils import get_page_link

router = APIRouter(prefix="", include_in_schema=False)
templates = Jinja2Templates(directory="src/templates/")

@router.post("/test")
async def test(theatre_id: str = Form(...)):
    return {"data": theatre_id}

@router.get("/show")
async def get_shows(request: Request, session: AsyncSession = Depends(get_async_session),
                     skip: int = Query(0, title="Skip"),
                 limit: int = Query(10, title="Limit")):
    shows = await src.crud.get_shows(session, skip=skip, limit=limit)
    new_shows = []
    for show in shows:
        new_show = dict(show)
        new_show['movie_title'] = (await src.crud.get_movie_by_id(session, show['movie_id']))['title']
        new_show['theatre_name'] = (await src.crud.get_theatre_by_id(session, show['theatre_id']))['theatre_name']
        new_show['format'] = (await src.crud.get_format_by_id(session, show['format_id']))['format_name']
        new_shows.append(new_show)
    next_link = ''
    prev_link = ''
    if limit == len(shows):
        new_skip_next = skip + limit
        next_link = get_page_link(new_skip_next, limit, 'movie')
    if skip > 0:
        new_skip_prev = skip - limit
        if new_skip_prev < 0: new_skip_prev = 0
        prev_link = get_page_link(new_skip_prev, limit, 'movie')
    return templates.TemplateResponse("show/index.html", {"request": request, "shows": new_shows, "next_link":next_link, "prev_link":prev_link})

@router.get("/show/{show_id}")
async def show_details(show_id: int, request: Request, session: AsyncSession = Depends(get_async_session)):
    return templates.TemplateResponse("show/details.html", {"request": request, "show": await src.crud.get_show_by_id(session, show_id)})


@router.get("/show/{show_id}/delete")
async def show_delete(show_id: int, request: Request, session: AsyncSession = Depends(get_async_session)):
    return templates.TemplateResponse("show/delete.html", {"request": request, "show": await src.crud.get_show_by_id(session, show_id)})

@router.post("/show/{show_id}/delete")
async def show_delete_submit(show_id: int, session: AsyncSession = Depends(get_async_session)):
    await src.crud.delete_show(session, show_id)
    return RedirectResponse("/show", status_code=303)


@router.get("/show/{show_id}/edit")
async def edit_show(request: Request, show_id: int, session: AsyncSession = Depends(get_async_session)):
    show = await src.crud.get_show_by_id(session, show_id)
    if show is not None:
        return templates.TemplateResponse("show/edit.html", {"request": request, "show": show})
    else:
        return {"message": "show not found"}

@router.post("/show/{show_id}/edit")
async def update_show(request: Request, show_id:int, theatre_id: int = Form(...), movie_id: int = Form(...), hall: int = Form(...),
                           date: date = Form(...),time: time = Form(...),format_id: int = Form(...),
                           price: float = Form(...), session: AsyncSession = Depends(get_async_session)):
    updated_show = Show_create(theatre_id=theatre_id,movie_id=movie_id,hall=hall,date=date,time=time,format_id=format_id,price=price)
    show = await src.crud.update_show_details(session, show_id, updated_show)
    if show is not None:
        return templates.TemplateResponse("show/edit.html", {"request": request, "show": show})
    else:
        return {"message": "show not found"}


@router.get("/show-create")
async def add_show(request: Request):
    return templates.TemplateResponse("show/create.html", {"request": request})

@router.post("/show-create")
async def submit_add_show(theatre_id: int = Form(...), movie_id: int = Form(...), hall_id: int = Form(...),
                           date: date = Form(...),time: time = Form(...),format_id: int = Form(...),
                           price: float = Form(...), session: AsyncSession = Depends(get_async_session)):
    new_show = Show_create(theatre_id=theatre_id, movie_id=movie_id,hall_id=hall_id,date=date,time=time,format_id=format_id,price=price)
    await src.crud.create_show(session, new_show)
    return RedirectResponse("/show", status_code=303)
