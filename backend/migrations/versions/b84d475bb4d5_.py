"""empty message

Revision ID: b84d475bb4d5
Revises:
Create Date: 2017-08-11 20:20:10.444948

"""
# coding: utf-8
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b84d475bb4d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    country_table = op.create_table('country',
                                    sa.Column('id', sa.Integer(), nullable=False),
                                    sa.Column('country', sa.String(length=100), nullable=False),
                                    sa.PrimaryKeyConstraint('id'))

    reason_table = op.create_table('reason',
                                   sa.Column('id', sa.Integer(), nullable=False),
                                   sa.Column('reason', sa.String(length=100), nullable=False),
                                   sa.PrimaryKeyConstraint('id'))

    type_called_table = op.create_table('type_called',
                                        sa.Column('id', sa.Integer(), nullable=False),
                                        sa.Column('type', sa.String(length=100), nullable=False),
                                        sa.PrimaryKeyConstraint('id'))

    op.create_table('record_called',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('type_called_id', sa.Integer(), nullable=True),
                    sa.Column('country_id', sa.Integer(), nullable=True),
                    sa.Column('reason_id', sa.Integer(), nullable=True),
                    sa.Column('text', sa.Text(), nullable=False),
                    sa.Column('created_date', sa.DateTime(), nullable=True),
                    sa.Column('update_date', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),
                    sa.ForeignKeyConstraint(['reason_id'], ['reason.id'], ),
                    sa.ForeignKeyConstraint(['type_called_id'], ['type_called.id'], ),
                    sa.PrimaryKeyConstraint('id'))

    op.bulk_insert(type_called_table, [
        {'id': 1, 'type': 'Telefone'},
        {'id': 2, 'type': 'Email'},
        {'id': 3, 'type': 'Chat'},
    ])

    op.bulk_insert(country_table, [
        {'id': 1, 'country': 'RJ'},
        {'id': 2, 'country': 'ES'},
    ])

    op.bulk_insert(reason_table, [
        {'id': 1, 'reason': 'Dúvidas'},
        {'id': 2, 'reason': 'Elogios'},
        {'id': 3, 'reason': 'Sugestões'},
    ])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('record_called')
    op.drop_table('type_called')
    op.drop_table('reason')
    op.drop_table('country')
    # ### end Alembic commands ###
