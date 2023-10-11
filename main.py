from fastapi import FastAPI
from fastapi.params import Body


app = FastAPI()


@app.get("/")
def say_hello():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"data": "this is the post"}


@app.post("/create_post")
def create_post(payload: dict = Body(...)):
    print(payload)

    return {"message": "success created post."}
