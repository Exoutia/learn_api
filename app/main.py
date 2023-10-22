from fastapi import FastAPI

from . import models
from .database import engine
from .routers import auth, posts, users

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)


@app.get("/")
def say_hello():
    return {"message": "post app"}
