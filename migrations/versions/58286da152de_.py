"""empty message

Revision ID: 58286da152de
Revises: 21ee2052357b
Create Date: 2019-09-22 02:29:07.642221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58286da152de'
down_revision = '21ee2052357b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('techs', sa.Column('in_prod', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('techs', 'in_prod')
    # ### end Alembic commands ###
