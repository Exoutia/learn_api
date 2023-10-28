"""creating sequence for user and posts

Revision ID: f8f7550a8fe5
Revises: 363fd2c380cd
Create Date: 2023-10-28 15:52:05.988302

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "f8f7550a8fe5"
down_revision: Union[str, None] = "363fd2c380cd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.schema.CreateSequence(sa.Sequence("post_id_seq")))
    op.execute(sa.schema.CreateSequence(sa.Sequence("user_id_seq")))


def downgrade() -> None:
    op.execute(sa.schema.DropSequence(sa.Sequence("post_id_seq")))
    op.execute(sa.schema.DropSequence(sa.Sequence("user_id_seq")))
