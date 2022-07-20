"""create new table post

Revision ID: e2f77f424221
Revises: 2683d5f2b63f
Create Date: 2022-07-20 10:52:38.650047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2f77f424221'
down_revision = '2683d5f2b63f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts",
    sa.Column("id",sa.String,primary_key=True, nullable=False, unique=True),
    sa.Column('content',sa.String,nullable=True,unique=True),
    sa.Column('hash',sa.String,nullable=False,unique=True),
    sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False, server_default=sa.text('now()')),
    sa.Column('published',sa.Boolean,server_default='TRUE', nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('post')
    pass
