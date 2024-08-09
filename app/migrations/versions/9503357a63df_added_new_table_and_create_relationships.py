"""added new table and create relationships

Revision ID: 9503357a63df
Revises: 
Create Date: 2024-08-09 17:51:31.514206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9503357a63df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('insta', sa.String(length=50), nullable=True),
    sa.Column('facebook', sa.String(length=50), nullable=True),
    sa.Column('youtube', sa.String(length=50), nullable=True),
    sa.Column('snapchat', sa.String(length=50), nullable=True),
    sa.Column('followers', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['influencer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('influencer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('password', sa.String(length=60), nullable=False))
        batch_op.add_column(sa.Column('role', sa.String(length=20), nullable=True))
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('bio',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=200),
               existing_nullable=False)
        batch_op.create_foreign_key(None, 'user', ['username'], ['username'])
        batch_op.drop_column('facebook')
        batch_op.drop_column('followers')
        batch_op.drop_column('snapchat')
        batch_op.drop_column('insta')
        batch_op.drop_column('platform')
        batch_op.drop_column('youtube')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('influencer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('youtube', sa.VARCHAR(length=50), nullable=True))
        batch_op.add_column(sa.Column('platform', sa.VARCHAR(length=60), nullable=False))
        batch_op.add_column(sa.Column('insta', sa.VARCHAR(length=50), nullable=True))
        batch_op.add_column(sa.Column('snapchat', sa.VARCHAR(length=50), nullable=True))
        batch_op.add_column(sa.Column('followers', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('facebook', sa.VARCHAR(length=50), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('bio',
               existing_type=sa.String(length=200),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.drop_column('role')
        batch_op.drop_column('password')
        batch_op.drop_column('id')

    op.drop_table('profiles')
    # ### end Alembic commands ###
