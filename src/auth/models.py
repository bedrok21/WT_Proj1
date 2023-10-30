from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None

class User(BaseModel):
    email: str | None = None

class UserInDB(User):
    password: str

class UserCreate(BaseModel):
    email:str
    password:str
