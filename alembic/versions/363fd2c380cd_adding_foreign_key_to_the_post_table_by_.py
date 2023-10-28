"""adding foreign key to the post table by users

Revision ID: 363fd2c380cd
Revises: f6fd31923866
Create Date: 2023-10-28 13:46:54.309688

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '363fd2c380cd'
down_revision: Union[str, None] = 'f6fd31923866'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
