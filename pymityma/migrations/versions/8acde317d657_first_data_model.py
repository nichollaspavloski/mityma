"""first data model

Revision ID: 8acde317d657
Revises: 
Create Date: 2022-11-15 00:12:36.417081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8acde317d657'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('location',
    sa.Column('id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('street', sa.String(), nullable=False),
    sa.Column('no', sa.String(), nullable=False),
    sa.Column('zip_code', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('person',
    sa.Column('id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('person_name', sa.String(), nullable=False),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('external_id', sa.String(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('location_id', sa.BigInteger(), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planting_area',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('area_name', sa.String(), nullable=False),
    sa.Column('location_id', sa.BigInteger(), nullable=False),
    sa.Column('is_public', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planting_area_plat',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('planting_area_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['planting_area_id'], ['planting_area.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('producer',
    sa.Column('id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('person_id', sa.BigInteger(), nullable=False),
    sa.Column('is_mentor', sa.Boolean(), nullable=False),
    sa.Column('show_location', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purchaser',
    sa.Column('id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('person_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('green',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('green_name', sa.String(), nullable=False),
    sa.Column('available', sa.Boolean(), nullable=False),
    sa.Column('deadline', sa.Date(), nullable=True),
    sa.Column('picked', sa.DateTime(), nullable=True),
    sa.Column('producer_id', sa.Integer(), nullable=False),
    sa.Column('pic_path', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['producer_id'], ['producer.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('producer_plat',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('producer_id', sa.Integer(), nullable=False),
    sa.Column('plat_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['plat_id'], ['planting_area_plat.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['producer_id'], ['producer.id'], ondelete='CASCADE'),
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
