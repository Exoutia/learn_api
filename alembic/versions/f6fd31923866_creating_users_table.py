"""creating users table

Revision ID: f6fd31923866
Revises: 8d43c474259e
Create Date: 2023-10-28 13:25:01.254814

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "f6fd31923866"
down_revision: Union[str, None] = "8d43c474259e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column(
            "uuid",
            sa.dialects.postgresql.UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
            server_default=sa.text("gen_random_uuid()"),
        ),
        sa.Column("id", sa.Integer, sa.Sequence("user_id_seq"), nullable=False),
        sa.Column("username", sa.String(255), nullable=False),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.UniqueConstraint("username"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("users")
