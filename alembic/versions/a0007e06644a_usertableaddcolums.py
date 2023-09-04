"""usertableaddcolums

Revision ID: a0007e06644a
Revises: 8dfdfdb78993
Create Date: 2023-09-04 19:07:41.662066

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0007e06644a'
down_revision: Union[str, None] = '8dfdfdb78993'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users',  
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False), 
                  )
    pass


def downgrade() -> None:
    op.drop_column('users', 'password','created-at',)
    pass
