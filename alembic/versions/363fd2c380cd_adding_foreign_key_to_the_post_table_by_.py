"""adding foreign key to the post table by users

Revision ID: 363fd2c380cd
Revises: f6fd31923866
Create Date: 2023-10-28 13:46:54.309688

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "363fd2c380cd"
down_revision: Union[str, None] = "f6fd31923866"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column(
            "user_uid",
            sa.dialects.postgresql.UUID(as_uuid=True),
            nullable=False,
        ),
    )
    op.create_foreign_key(
        "post_user_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["user_uid"],
        remote_cols=["uuid"],
        ondelete="CASCADE",
    )


def downgrade() -> None:
    op.drop_column("posts", "user_uid"),
    op.drop_constraint("post_user_fk", "posts", type_="foreignkey")
