"""add foreign-key to table posts

Revision ID: d31740e5c92e
Revises: e2f77f424221
Create Date: 2022-07-20 11:20:32.369131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd31740e5c92e'
down_revision = 'e2f77f424221'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("user_id",sa.String,nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'user_id'], remote_cols=['id'], ondelete="CASCADE")
    
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'user_id')
    pass
