"""poststable

Revision ID: 4b6742cd6315
Revises: 
Create Date: 2023-09-04 18:41:34.545389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b6742cd6315'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title',sa.String(), nullable=False))
    pass


def downgrade() -> None:
    pass
