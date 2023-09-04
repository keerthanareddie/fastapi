"""add content column

Revision ID: ca7e3034f674
Revises: 4b6742cd6315
Create Date: 2023-09-04 18:54:58.120391

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca7e3034f674'
down_revision: Union[str, None] = '4b6742cd6315'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
