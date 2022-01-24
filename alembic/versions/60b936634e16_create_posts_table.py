"""Create posts table

Revision ID: 60b936634e16
Revises: 
Create Date: 2022-01-24 09:41:45.459346

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '60b936634e16'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(
    ), primary_key=True), sa.Column('title', sa.String(), nullable=False),  sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
