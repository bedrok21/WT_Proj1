from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from .api_routes import router as api_router
from .controllers import movie_router, theatre_router, show_router
from .auth.auth_routes import auth_google_router
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="bjwlkekvpomecwdwada")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

app.include_router(api_router)

app.include_router(movie_router)
app.include_router(theatre_router)
app.include_router(show_router)

app.include_router(auth_google_router)


@app.on_event("startup")
async def startup1():
    redis = aioredis.from_url("redis://localhost", encoding= "utf8", decode_responce = True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cashe")
