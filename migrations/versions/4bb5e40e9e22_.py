"""empty message

Revision ID: 4bb5e40e9e22
Revises: 98ea4ee8e378
Create Date: 2018-11-22 09:52:56.043866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bb5e40e9e22'
down_revision = '98ea4ee8e378'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('seat_order',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('s_user', sa.Integer(), nullable=True),
    sa.Column('s_paidang', sa.Integer(), nullable=True),
    sa.Column('s_price', sa.Float(), nullable=True),
    sa.Column('s_seats', sa.String(length=128), nullable=True),
    sa.Column('s_status', sa.Integer(), nullable=True),
    sa.Column('s_expire', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['s_paidang'], ['pai_dang.id'], ),
    sa.ForeignKeyConstraint(['s_user'], ['viewer_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('seat_order')
    # ### end Alembic commands ###