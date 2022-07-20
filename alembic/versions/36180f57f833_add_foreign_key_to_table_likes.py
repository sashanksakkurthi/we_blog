"""add foreign-key to table likes

Revision ID: 36180f57f833
Revises: 2f83bf4c9953
Create Date: 2022-07-20 11:27:52.323743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36180f57f833'
down_revision = '2f83bf4c9953'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("likes",sa.Column("post_id",sa.String,nullable=False))
    op.add_column("likes",sa.Column("user_id",sa.String,nullable=False))
    op.create_foreign_key('like_users_fk', source_table="likes", referent_table="users", local_cols=[
                          'user_id'], remote_cols=['hash'], ondelete="CASCADE")
    op.create_foreign_key('like_posts_fk', source_table="likes", referent_table="users", local_cols=[
                          'post_id'], remote_cols=['hash'], ondelete="CASCADE")
    pass


    
def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="likes")
    op.drop_column('likes', 'user_id')
    op.drop_constraint('like_posts_fk', table_name="likes")
    op.drop_column('likes', 'post_id')
    pass
