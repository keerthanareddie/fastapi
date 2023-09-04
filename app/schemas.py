from pydantic import BaseModel, EmailStr
from typing import Optional
from pydantic.types import conint

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    #rating: Optional[int] = None

class PostCreate(PostBase):
    pass

class Userresponse(BaseModel):
    email: EmailStr
    class config:
        orm_mode=True

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    published : bool
    owner_id : int
    owner: Userresponse

    class config:
        orm_mode=True

class Postvote(BaseModel):
    Post: PostResponse
    votes: int

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type:str

class Tokendata(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

