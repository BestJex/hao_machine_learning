"""empty message

Revision ID: 1b77ec5319db
Revises: 
Create Date: 2020-09-22 18:25:58.615744

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1b77ec5319db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.BIGINT(unsigned=True), nullable=False, comment='用户主键'),
    sa.Column('username', sa.String(length=64), nullable=True, comment='用户账号名'),
    sa.Column('password_hash', sa.String(length=128), nullable=True, comment='用户密码'),
    sa.Column('is_admin', sa.Boolean(), nullable=True, comment='是否是超级管理员'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###