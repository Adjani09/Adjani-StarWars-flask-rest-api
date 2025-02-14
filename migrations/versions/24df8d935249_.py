"""empty message

Revision ID: 24df8d935249
Revises: a5cffa318ac2
Create Date: 2024-02-03 03:49:21.616149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24df8d935249'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('birth_year', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(), nullable=False),
    sa.Column('eye_color', sa.String(), nullable=False),
    sa.Column('hair_color', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('climate', sa.String(), nullable=False),
    sa.Column('gravity', sa.String(), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('terrain', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('favorite_people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('people_name', sa.String(length=120), nullable=True),
    sa.Column('user_email', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['people_name'], ['people.name'], ),
    sa.ForeignKeyConstraint(['user_email'], ['user.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite_planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planets_name', sa.String(length=120), nullable=True),
    sa.Column('user_email', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['planets_name'], ['planets.name'], ),
    sa.ForeignKeyConstraint(['user_email'], ['user.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite_planets')
    op.drop_table('favorite_people')
    op.drop_table('planets')
    op.drop_table('people')
    # ### end Alembic commands ###
