"""empty message

Revision ID: 076e3b200394
Revises: a4361e0dbebb
Create Date: 2024-04-02 14:49:42.913352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '076e3b200394'
down_revision = 'a4361e0dbebb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('genre')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genre',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='genre_pkey')
    )
    op.drop_table('Genre')
    # ### end Alembic commands ###