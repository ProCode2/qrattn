"""update schema

Revision ID: edc39d0c5c1f
Revises: 34ca8bd72cc4
Create Date: 2023-04-21 08:56:18.097032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edc39d0c5c1f'
down_revision = '34ca8bd72cc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('attendance', schema=None) as batch_op:
        batch_op.add_column(sa.Column('verified', sa.Boolean(), nullable=False))
        batch_op.alter_column('professor_id',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('student_id',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('class_id',
               existing_type=sa.TEXT(),
               nullable=False)

    with op.batch_alter_table('class', schema=None) as batch_op:
        batch_op.add_column(sa.Column('creatorId', sa.Text(), nullable=False))
        batch_op.add_column(sa.Column('studentIds', sa.Text(), nullable=False))
        batch_op.add_column(sa.Column('startTime', sa.DateTime(timezone=True), nullable=False))
        batch_op.add_column(sa.Column('endTime', sa.DateTime(timezone=True), nullable=False))
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=128), nullable=False))
        batch_op.add_column(sa.Column('location', sa.Text(), nullable=False))
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('role',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)
        batch_op.create_unique_constraint("email", ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('role',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.drop_column('location')
        batch_op.drop_column('email')

    with op.batch_alter_table('class', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
        batch_op.drop_column('endTime')
        batch_op.drop_column('startTime')
        batch_op.drop_column('studentIds')
        batch_op.drop_column('creatorId')

    with op.batch_alter_table('attendance', schema=None) as batch_op:
        batch_op.alter_column('class_id',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.alter_column('student_id',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.alter_column('professor_id',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.drop_column('verified')

    # ### end Alembic commands ###
