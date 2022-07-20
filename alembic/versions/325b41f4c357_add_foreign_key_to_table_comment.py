"""add foreign key to table comment

Revision ID: 325b41f4c357
Revises: df5e47fd15ba
Create Date: 2022-07-20 11:41:53.163872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '325b41f4c357'
down_revision = 'df5e47fd15ba'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("comments",sa.Column("post_id",sa.String,nullable=False))
    op.add_column("comments",sa.Column("user_id",sa.String,nullable=False))
    op.create_foreign_key('like_users_fk', source_table="comments", referent_table="users", local_cols=[
                          'user_id'], remote_cols=['hash'], ondelete="CASCADE")
    op.create_foreign_key('like_posts_fk', source_table="comments", referent_table="users", local_cols=[
                          'post_id'], remote_cols=['hash'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="comments")
    op.drop_column('comments', 'user_id')
    op.drop_constraint('like_posts_fk', table_name="comments")
    op.drop_column('comments', 'post_id')
    pass
