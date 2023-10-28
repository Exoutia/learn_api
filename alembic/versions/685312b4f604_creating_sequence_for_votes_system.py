"""creating table for votes system 
with the foreign keys to users and posts table.

Revision ID: 685312b4f604
Revises: f8f7550a8fe5
Create Date: 2023-10-28 18:30:48.432447

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "685312b4f604"
down_revision: Union[str, None] = "f8f7550a8fe5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "votes",
        sa.Column(
            "user_uid",
            sa.dialects.postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.uuid", ondelete="CASCADE"),
            primary_key=True,
            nullable=False,
        ),
        sa.Column(
            "post_uid",
            sa.dialects.postgresql.UUID(as_uuid=True),
            sa.ForeignKey("posts.uuid", ondelete="CASCADE"),
            primary_key=True,
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_table("votes")
