from pydantic import BaseModel, UUID4
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class Post(PostBase):
    uuid: UUID4
    id: int
    rating: int | None = None
    created_at: datetime

    class Config:
        from_attributes = True


class CreatePost(PostBase):
    class Config:
        from_attributes = True


class UpdatePost(PostBase):
    pass
