"""projects and techs

Revision ID: 464ae39bedd6
Revises: 
Create Date: 2019-09-18 17:48:41.303675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '464ae39bedd6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('desc', sa.String(length=2000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_project_title'), 'project', ['title'], unique=True)
    op.create_table('tech',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('icon', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tech_icon'), 'tech', ['icon'], unique=True)
    op.create_index(op.f('ix_tech_name'), 'tech', ['name'], unique=True)
    op.create_table('association',
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('tech_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['tech_id'], ['tech.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association')
    op.drop_index(op.f('ix_tech_name'), table_name='tech')
    op.drop_index(op.f('ix_tech_icon'), table_name='tech')
    op.drop_table('tech')
    op.drop_index(op.f('ix_project_title'), table_name='project')
    op.drop_table('project')
    # ### end Alembic commands ###
