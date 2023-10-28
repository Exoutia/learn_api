from fastapi import FastAPI

from . import models
from .database import engine
from .routers import auth, posts, users, votes

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)


@app.get("/")
def say_hello():
    return {"message": "post app"}


# this is a test comment
