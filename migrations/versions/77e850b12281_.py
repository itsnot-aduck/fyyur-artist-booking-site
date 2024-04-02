"""empty message

Revision ID: 77e850b12281
Revises: 9aba90b9307d
Create Date: 2024-04-03 00:57:48.529632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77e850b12281'
down_revision = '9aba90b9307d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'seeking_talent',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'seeking_talent',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###