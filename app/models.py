from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Column,
    ForeignKey,
    Integer,
    Sequence,
    String,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base


class Post(Base):
    __tablename__ = "posts"

    uuid = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    id = Column(Integer, Sequence("post_id_seq"))
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, server_default="TRUE")
    rating = Column(Integer, nullable=True)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    user_uid = Column(
        UUID(as_uuid=True), ForeignKey("users.uuid", ondelete="CASCADE"), nullable=False
    )
    user = relationship("User")
    __table_args__ = (
        CheckConstraint("rating >= 0 and rating <= 5", name="check_rating_range"),
    )


class User(Base):
    __tablename__ = "users"
    uuid = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    id = Column(Integer, Sequence("user_id_seq"))
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    def __repr__(self):
        return f"""<User {self.username},
                    \ncreated_at {self.created_at},
                    \nid {self.id},
                    \nuuid {self.uuid},
                >
                """


class Vote(Base):
    __tablename__ = "votes"
    post_uid = Column(
        UUID(as_uuid=True),
        ForeignKey("posts.uuid", ondelete="CASCADE"),
        primary_key=True,
    )
    user_uid = Column(
        UUID(as_uuid=True),
        ForeignKey("users.uuid", ondelete="CASCADE"),
        primary_key=True,
    )
    user = relationship("User")
    post = relationship("Post")
