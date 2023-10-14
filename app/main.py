from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from time import sleep
from uuid import uuid4

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: int | None = None


while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="learn_api",
            user="postgres",
            cursor_factory=RealDictCursor,
        )
        cursor = conn.cursor()
        print("database connection was successful")
        break
    except psycopg2.Error as e:
        print(f"I am unable to connect to the database {e}")
        sleep(2)


@app.get("/")
def say_hello():
    return {"message": "post app"}


@app.get("/posts")
def get_posts():
    cursor.execute("SELECT * FROM posts")
    my_posts = cursor.fetchall()
    return {"data": my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    uuid = str(uuid4())
    title = post.title
    content = post.content
    published = post.published
    rating = post.rating
    cursor.execute(
        """INSERT INTO posts (uuid, title, content, published, rating)
        VALUES (%s, %s, %s, %s, %s) RETURNING *""",
        (uuid, title, content, published, rating),
    )
    post_created = cursor.fetchone()
    cursor.commit()
    return {
        "post_u_id": post_created["uuid"],
        "post_id": post_created["id"],
        "data": post_created,
    }


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    cursor.execute("SELECT * FROM posts WHERE id = %s", (post_id,))
    post = cursor.fetchone()
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {post_id} not found",
        )
    else:
        return {"data": post}


@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int):
    cursor.execute("DELETE FROM posts WHERE id = %s RETURNING *", (post_id,))
    post = cursor.fetchone()
    print(post)
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {post_id} not found",
        )
    else:
        return


@app.put("/posts/{post_id}", status_code=status.HTTP_202_ACCEPTED)
def update_post(post_id: int, post: Post):
    cursor.execute(
        """UPDATE posts SET title = %s, content = %s
            WHERE id = %s RETURNING *""",
        (post.title, post.content, post_id),
    )
    updated_post = cursor.fetchone()
    if updated_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {post_id} not found",
        )
    else:
        return {"message": "post updated successfully", "data": updated_post}
