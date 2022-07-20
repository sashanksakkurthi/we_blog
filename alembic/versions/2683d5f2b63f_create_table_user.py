"""create table user

Revision ID: 2683d5f2b63f
Revises: 
Create Date: 2022-07-19 11:28:15.074611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2683d5f2b63f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id',sa.String,primary_key=True,nullable=False,unique=True),
    sa.Column('email',sa.String,nullable=False,unique=True),
    sa.Column('name',sa.String,nullable=False),
    sa.Column('hash',sa.String,nullable=False,unique=True),
    sa.Column('password',sa.String,nullable=False),
    sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False, server_default=sa.text('now()')),
    sa.Column('verified',sa.Boolean,server_default='FALSE',nullable=False),
    sa.Column('active',sa.Boolean,server_default='TRUE',nullable=False),
    )
    pass

def downgrade() -> None:
    op.drop_table('user')
    pass