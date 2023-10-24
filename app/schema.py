from datetime import datetime

from pydantic import UUID4, BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr


class User(UserBase):
    uuid: UUID4
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class PostUserOut(UserBase):
    id: int


class CreateUser(UserBase):
    password: str

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class Post(PostBase):
    uuid: UUID4
    id: int
    rating: int | None = None
    created_at: datetime
    user_uid: UUID4
    user: PostUserOut

    class Config:
        from_attributes = True


class CreatePost(PostBase):
    class Config:
        from_attributes = True


class UpdatePost(PostBase):
    pass


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
