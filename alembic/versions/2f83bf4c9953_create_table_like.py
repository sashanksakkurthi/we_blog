"""create table like

Revision ID: 2f83bf4c9953
Revises: d31740e5c92e
Create Date: 2022-07-20 11:23:47.960692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f83bf4c9953'
down_revision = 'd31740e5c92e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('likes',
    sa.Column("id",sa.String,primary_key=True, nullable=False, unique=True),
    sa.Column("hash",sa.String,nullable=False, unique=True))
    pass


def downgrade() -> None:
    op.drop_table('likes')
    pass
