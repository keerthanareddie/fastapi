"""uc

Revision ID: a27462ceddb0
Revises: a0007e06644a
Create Date: 2023-09-04 19:20:46.787201

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a27462ceddb0'
down_revision: Union[str, None] = 'a0007e06644a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users',  
                  sa.Column('password', sa.String(), nullable=False), 
                  )
    pass


def downgrade() -> None:
    op.drop_column('users', 'password')
    pass
