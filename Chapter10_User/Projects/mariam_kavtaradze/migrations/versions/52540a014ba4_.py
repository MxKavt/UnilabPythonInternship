"""empty message

Revision ID: 52540a014ba4
Revises: 
Create Date: 2022-07-30 18:41:03.828736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52540a014ba4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=24), nullable=True),
    sa.Column('email', sa.String(length=48), nullable=True),
    sa.Column('password', sa.String(length=48), nullable=True),
    sa.Column('experience', sa.String(length=24), nullable=True),
    sa.Column('account_type', sa.String(length=24), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
