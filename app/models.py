from .database import Base
from uuid import uuid4
from sqlalchemy import Column, Integer, String, Boolean, CheckConstraint, Sequence
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import text


class Post(Base):
    __tablename__ = "posts"

    uuid = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )
    id = Column(Integer, Sequence("post_id_seq"))
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, server_default="TRUE")
    rating = Column(Integer, nullable=True)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    __table_args__ = (
        CheckConstraint("rating >= 0 and rating <= 5", name="check_rating_range"),
    )


class User(Base):
    __tablename__ = "users"
    uuid = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )
    id = Column(Integer, Sequence("user_id_seq"))
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    salt = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
