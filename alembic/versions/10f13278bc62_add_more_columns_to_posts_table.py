"""Add more columns to posts table

Revision ID: 10f13278bc62
Revises: 88e1382f9dac
Create Date: 2022-01-24 12:23:38.089017

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '10f13278bc62'
down_revision = '88e1382f9dac'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
