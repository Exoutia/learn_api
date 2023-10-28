"""create post table

Revision ID: 0beb3337f971
Revises:
Create Date: 2023-10-28 08:34:34.502971

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "0beb3337f971"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column(
            "uuid",
            sa.dialects.postgresql.UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
            server_default=sa.text("gen_random_uuid()"),
        ),
        sa.Column("id", sa.Integer, sa.Sequence('post_seq_id'), nullable=False),
        sa.Column("title", sa.String(255), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("posts")
