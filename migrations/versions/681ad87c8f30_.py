"""empty message

Revision ID: 681ad87c8f30
Revises: 476faf5a4553
Create Date: 2022-10-14 15:40:20.390613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '681ad87c8f30'
down_revision = '476faf5a4553'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('climate', sa.String(length=250), nullable=True),
    sa.Column('gravity', sa.String(length=250), nullable=True),
    sa.Column('terrain', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###