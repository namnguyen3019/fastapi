"""add foreign key to posts table

Revision ID: 28d7054e963a
Revises: de38325595d0
Create Date: 2022-01-24 11:06:52.229421

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '28d7054e963a'
down_revision = 'de38325595d0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users",
                          local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', "owner_id")
    pass
