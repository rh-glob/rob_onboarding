"""
Added customer_id field to OrderEvent

Revision ID: 0ab6b8751137
Revises: c04345bd5fc8
Create Date: 2019-11-05 09:55:43.825169

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op
# revision identifiers, used by Alembic.
from microcosm_postgres.identifiers import new_object_id


revision = '0ab6b8751137'
down_revision = 'c04345bd5fc8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    assert False, 'This migration needs to be fixed before running'
    op.add_column(
        'order_event', sa.Column(
            'customer_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True,
        )

    )
    # TODO: Fix this migration
    # populate customer_id with UUID value
    #op.execute('UPDATE order_event SET customer_id = ')
    # set column to nullable=False
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order_event', 'customer_id')
    # ### end Alembic commands ###