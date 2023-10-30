"""Init1

Revision ID: 5c699dafd489
Revises: 
Create Date: 2023-10-29 17:00:39.936741

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c699dafd489'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('format',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('format_name', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hall',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hall_num', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=250), nullable=False),
    sa.Column('description', sa.String(length=2000), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('picture', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('permissions', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status_name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('theatre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('theatre_name', sa.String(length=250), nullable=False),
    sa.Column('location', sa.String(length=500), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longtitude', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(length=1024), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('theatre_id', sa.Integer(), nullable=True),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('hall_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('time', sa.Time(), nullable=False),
    sa.Column('format_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['format_id'], ['format.id'], ),
    sa.ForeignKeyConstraint(['hall_id'], ['hall.id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['theatre_id'], ['theatre.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('seat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('show_id', sa.Integer(), nullable=True),
    sa.Column('raw', sa.Integer(), nullable=False),
    sa.Column('seat', sa.Integer(), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['show_id'], ['show.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['status.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('seat')
    op.drop_table('show')
    op.drop_table('user')
    op.drop_table('theatre')
    op.drop_table('status')
    op.drop_table('role')
    op.drop_table('movie')
    op.drop_table('hall')
    op.drop_table('format')
    # ### end Alembic commands ###
