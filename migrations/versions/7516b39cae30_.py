"""empty message

Revision ID: 7516b39cae30
Revises: c9721e220d06
Create Date: 2021-09-15 15:25:38.321227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7516b39cae30'
down_revision = 'c9721e220d06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###