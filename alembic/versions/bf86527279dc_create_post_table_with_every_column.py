"""create post table with every column

Revision ID: bf86527279dc
Revises: 0beb3337f971
Create Date: 2023-10-28 11:30:25.049239

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bf86527279dc'
down_revision: Union[str, None] = '0beb3337f971'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
