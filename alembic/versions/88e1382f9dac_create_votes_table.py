"""Create votes table

Revision ID: 88e1382f9dac
Revises: 28d7054e963a
Create Date: 2022-01-24 11:13:41.301986

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '88e1382f9dac'
down_revision = '28d7054e963a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('votes', sa.Column('user_id', sa.Integer(
    ), primary_key=True), sa.Column('post_id', sa.Integer(), primary_key=True))
    op.create_foreign_key('votes_users_fk', "votes", "users", [
                          'user_id'], ['id'], ondelete="CASCADE")

    op.create_foreign_key('votes_posts_fk', "votes", "posts", [
                          'post_id'], ['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('votes_users_fk', 'votes')
    op.drop_constraint('votes_posts_fk', 'votes')
    op.drop_table('votes')
    pass
