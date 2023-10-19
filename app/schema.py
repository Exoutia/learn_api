from datetime import datetime

from pydantic import UUID4, BaseModel, EmailStr


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


class UserBase(BaseModel):
    username: str
    email: EmailStr


class User(UserBase):
    uuid: UUID4
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class CreateUser(UserBase):
    password: str

    class Config:
        from_attributes = True
