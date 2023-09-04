from fastapi import FastAPI
from . import models, schemas, utils
from .database import engine
from .routers import post, user, auth, vote
from .config import Settings
from fastapi.middleware.cors import CORSMiddleware
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)








# postlist = [{"title": "abc", "content": "testabc", "id": 1}, {"title": "def", "content": "defcontent", "id": 2}]

# def find_post(id):
#     for i in postlist:
#         if i['id'] == id:
#             return i 

# def find_index(id):
#     for j, p in enumerate(postlist):
#         if p["id"] == id:
#             return j        


@app.get("/")
def get_user():
    return {"message": "Hello World"}


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)