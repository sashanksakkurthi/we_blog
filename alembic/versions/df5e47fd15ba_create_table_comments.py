"""create table comments

Revision ID: df5e47fd15ba
Revises: 36180f57f833
Create Date: 2022-07-20 11:38:16.358015

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df5e47fd15ba'
down_revision = '36180f57f833'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("comments",
    sa.Column("id",sa.String,primary_key=True, nullable=False, unique=True),
    sa.Column("comment",sa.String,nullable=False,unique=False),
    sa.Column("hash",sa.String,nullable=False, unique=True)
    )
    pass


def downgrade() -> None:
    op.drop_table('comments')
    pass
