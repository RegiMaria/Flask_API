"""Descrição das alterações no modelo

Revision ID: 9315086c568f
Revises: 
Create Date: 2024-04-23 16:20:33.916668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9315086c568f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('senha_hash', sa.String(length=128), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('senha_hash')

    # ### end Alembic commands ###
