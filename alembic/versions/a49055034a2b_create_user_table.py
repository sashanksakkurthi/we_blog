"""create user  table

Revision ID: a49055034a2b
Revises: 
Create Date: 2022-07-18 11:21:26.056640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a49055034a2b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('user',
    sa.Column('id',sa.String,primary_key=True,nullable=False,unique=True),
    sa.Column('email',sa.String,nullable=False,unique=True),
    sa.Column('password',sa.String,nullable=False),
    sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False, server_default=sa.text('now()')),
    sa.Column('verified',sa.Boolean,server_default='FALSE',nullable=False),
    sa.Column('active',sa.Boolean,server_default='TRUE',nullable=False)
    )


def downgrade() -> None:
    op.drop_table('user')
