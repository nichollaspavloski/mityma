"""first data model

Revision ID: 54d4a58cd033
Revises: 
Create Date: 2022-11-07 20:44:49.585802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54d4a58cd033'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('location',
    sa.Column('id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('street', sa.String(), nullable=True),
    sa.Column('no', sa.String(), nullable=True),
    sa.Column('zip_code', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('person',
    sa.Column('id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('person_name', sa.String(), nullable=True),
    sa.Column('lastname', sa.String(), nullable=True),
    sa.Column('login', sa.String(), nullable=True),
    sa.Column('external_id', sa.String(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('location_id', sa.BigInteger(), nullable=True),
    sa.Column('creation_date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planting_area',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('area_name', sa.String(), nullable=True),
    sa.Column('location_id', sa.BigInteger(), nullable=True),
    sa.Column('is_public', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planting_area_plat',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('planting_area_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planting_area_id'], ['planting_area.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('producer',
    sa.Column('id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('person_id', sa.BigInteger(), nullable=True),
    sa.Column('is_mentor', sa.Boolean(), nullable=True),
    sa.Column('show_location', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purchaser',
    sa.Column('id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('person_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('green',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('green_name', sa.String(), nullable=True),
    sa.Column('available', sa.Boolean(), nullable=True),
    sa.Column('deadline', sa.Date(), nullable=True),
    sa.Column('picked', sa.Date(), nullable=True),
    sa.Column('producer_id', sa.Integer(), nullable=True),
    sa.Column('pic_path', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['producer_id'], ['producer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('producer_plat',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('producer_id', sa.Integer(), nullable=True),
    sa.Column('plat_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['plat_id'], ['planting_area_plat.id'], ),
    sa.ForeignKeyConstraint(['producer_id'], ['producer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('producer_plat')
    op.drop_table('green')
    op.drop_table('purchaser')
    op.drop_table('producer')
    op.drop_table('planting_area_plat')
    op.drop_table('planting_area')
    op.drop_table('person')
    op.drop_table('location')
    # ### end Alembic commands ###
