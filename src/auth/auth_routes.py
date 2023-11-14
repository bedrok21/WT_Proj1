from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from authlib.integrations.starlette_client import OAuth
from starlette.responses import RedirectResponse
from starlette.requests import Request
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta
from typing import Annotated
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from .utils import get_password_hash, verify_password
from .models import *


auth_google_router = APIRouter(prefix="", include_in_schema=False)

oauth = OAuth()
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_id='281277195128-2qcoek3a2pglohgt9n6sbigq2q61a30a.apps.googleusercontent.com',
    client_secret='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',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    token_url='https://accounts.google.com/o/oauth2/token',
    client_kwargs={
        'scope': 'openid email profile',
        'prompt': 'select_account',
    }
)

@auth_google_router.get("/login/google")
async def login_google(request: Request):
    redirect_uri = request.url_for('auth_google')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@auth_google_router.get("/auth/google")
async def auth_google(request: Request):
    token = await oauth.google.authorize_access_token(request)
    access_token = token.get('access_token')
    user_info = token.get('userinfo')
    request.session['token'] = (access_token)
    request.session['user_info'] = (user_info)
    return RedirectResponse(url='/movie')

@auth_google_router.get('/logout/google')
async def logout(request: Request):
    request.session.pop('token', None)
    request.session.pop('user_info', None)
    return RedirectResponse(url='/movie')

@auth_google_router.get('/')
async def landing():
    return {"message":"Ok"}
