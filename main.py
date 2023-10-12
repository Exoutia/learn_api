from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: int | None = None


@app.get("/")
def say_hello():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"data": "this is the post"}


@app.post("/create_post")
def create_post(post: Post):
    print(post)
    return {"data": "new post is created"}
