"""ownerid

Revision ID: 3b14205b8cfe
Revises: a27462ceddb0
Create Date: 2023-09-04 19:27:36.273129

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b14205b8cfe'
down_revision: Union[str, None] = 'a27462ceddb0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users-fk', table_name="posts")
    op.drop_column('posts','owner_id')
    pass
