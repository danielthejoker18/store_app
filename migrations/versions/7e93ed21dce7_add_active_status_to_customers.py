"""Add active status to customers

Revision ID: 7e93ed21dce7
Revises: 
Create Date: 2024-11-26 15:54:26.438820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e93ed21dce7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('customer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('active', sa.Boolean(), server_default=sa.text('1'), nullable=False))
        batch_op.add_column(sa.Column('inactivated_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('inactivation_reason', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('customer', schema=None) as batch_op:
        batch_op.drop_column('inactivation_reason')
        batch_op.drop_column('inactivated_at')
        batch_op.drop_column('active')

    # ### end Alembic commands ###
