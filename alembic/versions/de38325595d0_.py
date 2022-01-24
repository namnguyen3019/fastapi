"""empty message

Revision ID: de38325595d0
Revises: 60b936634e16
Create Date: 2022-01-24 10:43:07.148568

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'de38325595d0'
down_revision = '60b936634e16'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False), sa.Column('email', sa.String(), nullable=False), sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False), sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
