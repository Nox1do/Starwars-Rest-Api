"""empty message

Revision ID: 476faf5a4553
Revises: 642e3da6c798
Create Date: 2022-10-13 04:25:26.894084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '476faf5a4553'
down_revision = '642e3da6c798'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('characters', sa.Column('height', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('characters', 'height')
    # ### end Alembic commands ###
