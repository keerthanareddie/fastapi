"""add user table

Revision ID: 8dfdfdb78993
Revises: ca7e3034f674
Create Date: 2023-09-04 19:01:22.537650

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8dfdfdb78993'
down_revision: Union[str, None] = 'ca7e3034f674'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('email',sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
