from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from . import models, schemas


async def get_movies(session: AsyncSession, limit:int=20, skip:int=0):
    result = await session.execute(select(models.movie).limit(limit).offset(skip))
    return [r._mapping for r in result.all()]

async def create_movie(session: AsyncSession, new_movie: schemas.Movie_create):
    await session.execute(insert(models.movie).values(**new_movie.model_dump()))
    return await session.commit()

async def get_movie_by_id(session: AsyncSession, movie_id: int):
    result = await session.execute(select(models.movie).where(models.movie.c.id == movie_id))
    result = result.all()
    if len(result) > 0:
        return result[0]._mapping
    raise HTTPException(status_code=404, detail="Not Found")

async def update_movie_details(session: AsyncSession, movie_id:int, updated_movie: schemas.Movie_create):
    await session.execute(update(models.movie).where(models.movie.c.id==movie_id).values(**updated_movie.model_dump()))
    await session.commit()
    return await get_movie_by_id(session, movie_id)

async def delete_movie(session: AsyncSession, movie_id:int):
    await session.execute(delete(models.movie).where(models.movie.c.id==movie_id))
    await session.commit()

####################################################

async def get_theatres(session: AsyncSession):
    result = await session.execute(select(models.theatre))
    return [r._mapping for r in result.all()]

async def create_theatre(session: AsyncSession, new_theatre: schemas.Theatre_create):
    await session.execute(insert(models.theatre).values(**new_theatre.model_dump()))
    await session.commit()

async def get_theatre_by_id(session: AsyncSession, id: int):
    result = await session.execute(select(models.theatre).where(models.theatre.c.id == id))
    result = result.all()
    if len(result) > 0:
        return result[0]._mapping
    raise HTTPException(status_code=404, detail="Not Found")

async def update_theatre_details(session: AsyncSession, theatre_id:int, updated_theatre:schemas.Theatre_create):
    await session.execute(update(models.theatre).where(models.theatre.c.id==theatre_id).values(**updated_theatre.model_dump()))
    await session.commit()
    return await get_theatre_by_id(session, theatre_id)

async def delete_theatre(session: AsyncSession, theatre_id:int):
    await session.execute(delete(models.theatre).where(models.theatre.c.id==theatre_id))
    await session.commit()

####################################################

async def get_shows(session: AsyncSession, limit:int=10, skip:int=0):
    result = await session.execute(select(models.show).limit(limit).offset(skip))
    return [r._mapping for r in result.all()]

async def create_show(session: AsyncSession, new_show: schemas.Show_create):
    await session.execute(insert(models.show).values(**new_show.model_dump()))
    await session.commit()

async def get_show_by_id(session: AsyncSession, id: int):
    result = await session.execute(select(models.show).where(models.show.c.id == id))
    result = result.all()
    if len(result) > 0:
        return result[0]._mapping
    return None

async def update_show_details(session:AsyncSession, show_id:int, updated_show:schemas.Show_create):
    await session.execute(update(models.show).where(models.show.c.id==show_id).values(**updated_show.model_dump()))
    await session.commit()
    return await get_show_by_id(session, show_id)

async def delete_show(session: AsyncSession, show_id:int):
    await session.execute(delete(models.show).where(models.show.c.id==show_id))
    await session.commit()

async def get_shows_by_movie_id(session: AsyncSession, movie_id:int):
    result = await session.execute(select(models.show).where(models.show.c.movie_id==movie_id).limit(5).offset(0))
    return [r._mapping for r in result.all()]
####################################################

async def get_formats(session: AsyncSession):
    result = await session.execute(select(models.format))
    return [r._mapping for r in result.all()]

async def get_format_by_id(session: AsyncSession, id: int):
    result = await session.execute(select(models.format).where(models.format.c.id == id))
    result = result.all()
    if len(result) > 0:
        return result[0]._mapping
    return None

async def get_statuses(session: AsyncSession):
    result = await session.execute(select(models.status))
    return [r._mapping for r in result.all()]

async def get_genres(session: AsyncSession):
    result = await session.execute(select(models.genre))
    return [r._mapping for r in result.all()]

async def get_movie_genres(session: AsyncSession):
    result = await session.execute(select(models.movie_genre))
    return [r._mapping for r in result.all()]

async def create_movie_genre(session: AsyncSession, new_movie_genre: schemas.MovieGenre_create):
    await session.execute(insert(models.movie_genre).values(**new_movie_genre.model_dump()))
    await session.commit()

async def create_genre(session: AsyncSession, new_genre: schemas.Genre_create):
    await session.execute(insert(models.genre).values(**new_genre.model_dump()))
    await session.commit()

async def create_format(session: AsyncSession, new_format: schemas.Format_create):
    await session.execute(insert(models.format).values(**new_format.model_dump()))
    await session.commit()

async def create_status(session: AsyncSession, new_status: schemas.Status_create):
    await session.execute(insert(models.status).values(**new_status.model_dump()))
    await session.commit()

############################################



async def get_user_by_email(session: AsyncSession, email: str):
    result = await session.execute(select(models.user).where(models.user.c.email == email))
    result = result.all()
    if len(result) > 0:
        return result[0]._mapping
    return None

async def create_user(session:AsyncSession, new_user: schemas.UserCreate):
    await session.execute(insert(models.user).values(**new_user.model_dump()))
    return await session.commit()
