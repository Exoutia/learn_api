from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from random import randint


app = FastAPI()

# TODO: continue from here https://youtu.be/0sOvCWFmrtA?t=8508 
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: int | None = None


my_posts = {
    1: {
        "title": "post 1",
        "content": "this is the content of post 1",
        "published": True,
        "rating": 4,
    },
    2: {
        "title": "post 2",
        "content": "this is the content of post 2",
        "published": True,
        "rating": 5,
    },
    3: {
        "title": "post 3",
        "content": "this is the content of post 3",
        "published": True,
        "rating": 3,
    },
}


@app.get("/")
def say_hello():
    return {"message": "post app"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    print(post)
    post_dict = post.dict()
    id = randint(4, 100_000_000)
    my_posts[id] = post_dict
    return {"post_id": id, "post that you created": post_dict}


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    post = my_posts.get(post_id)
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {post_id} not found",
        )
    else:
        return {"data": post}


@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int):
    if post_id not in my_posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {post_id} not found",
        )
    else:
        del my_posts[post_id]
        return


@app.put("/posts/{post_id}", status_code=status.HTTP_202_ACCEPTED)
def update_post(post_id: int, post: Post):
    if post_id not in my_posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {post_id} not found",
        )
    else:
        post_dict = post.dict()
        my_posts[post_id] = post_dict
        return {"message": "post updated successfully", "data": post_dict}
