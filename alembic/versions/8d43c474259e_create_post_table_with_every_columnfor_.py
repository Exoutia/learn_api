"""create post table with every columnfor real this time.

Revision ID: 8d43c474259e
Revises: bf86527279dc
Create Date: 2023-10-28 11:58:33.930825

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "8d43c474259e"
down_revision: Union[str, None] = "bf86527279dc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean, server_default="TRUE", nullable=False),
    )
    op.add_column(
        "posts",
        sa.Column("rating", sa.Integer, nullable=True),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.sql.sqltypes.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "rating")
    op.drop_column("posts", "created_at")
