from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date, time
from src.database import get_async_session
from src.schemas import Theatre_create, Theatre
import src.crud

router = APIRouter(prefix="", include_in_schema=False)
templates = Jinja2Templates(directory="src/templates/")


@router.get("/theatre")
async def get_theatres(request: Request, session: AsyncSession = Depends(get_async_session)):
    return templates.TemplateResponse("theatre/index.html", {"request": request, "location":{"lat":49.233985,"lon":28.449593,"name":"NAME"},"theatres": await src.crud.get_theatres(session)})

@router.get("/theatre/{theatre_id}")
async def theatre_details(theatre_id: int, request: Request, session: AsyncSession = Depends(get_async_session)):
    return templates.TemplateResponse("theatre/details.html", {"request": request, "theatre": await src.crud.get_theatre_by_id(session, theatre_id)})


@router.get("/theatre/{theatre_id}/delete")
async def theatre_delete(theatre_id: int, request: Request, session: AsyncSession = Depends(get_async_session)):
    return templates.TemplateResponse("theatre/delete.html", {"request": request, "theatre": await src.crud.get_theatre_by_id(session, theatre_id)})

@router.post("/theatre/{theatre_id}/delete")
async def theatre_delete_submit(theatre_id: int, session: AsyncSession = Depends(get_async_session)):
    await src.crud.delete_theatre(session, theatre_id)
    return RedirectResponse("/theatre", status_code=303)


@router.get("/theatre/{theatre_id}/edit")
async def edit_theatre(request: Request, theatre_id: int, session: AsyncSession = Depends(get_async_session)):
    theatre = await src.crud.get_theatre_by_id(session, theatre_id)

    if theatre is not None:
        return templates.TemplateResponse("theatre/edit.html", {"request": request, "theatre": theatre})
    else:
        return {"message": "theatre not found"}

@router.post("/theatre/{theatre_id}/edit")
async def update_theatre(request: Request, theatre_id:int, theatre_name: str = Form(...),location: str = Form(...), latitude: float = Form(...),
                           longtitude: float = Form(...), session: AsyncSession = Depends(get_async_session)):
    updated_theatre = Theatre_create(theatre_name=theatre_name,location=location,latitude=latitude,longtitude=longtitude)
    theatre = await src.crud.update_theatre_details(session, theatre_id, updated_theatre)
    if theatre is not None:
        return templates.TemplateResponse("theatre/edit.html", {"request": request, "theatre": theatre})
    else:
        return {"message": "theatre not found"}


@router.get("/theatre-create")
async def add_theatre(request: Request):
    return templates.TemplateResponse("theatre/create.html", {"request": request})

@router.post("/theatre-create")
async def submit_add_theatre(theatre_name: str = Form(...),location: str = Form(...), latitude: float = Form(...),
                           longtitude: float = Form(...), session: AsyncSession = Depends(get_async_session)):
    new_theatre = Theatre_create(theatre_name=theatre_name, location=location, latitude=latitude, longtitude=longtitude)
    await src.crud.create_theatre(session, new_theatre)
    return RedirectResponse("/theatre", status_code=303)
