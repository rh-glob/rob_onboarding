"""
Added missing fields

Revision ID: 58399952de67
Revises: c04345bd5fc8
Create Date: 2019-11-05 15:41:06.897522

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op


# revision identifiers, used by Alembic.
revision = "58399952de67"
down_revision = "c04345bd5fc8"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "order_event",
        sa.Column(
            "customer_id",
            sqlalchemy_utils.types.uuid.UUIDType(),
            nullable=True,
        ),
    )
    op.add_column(
        "pizza",
        sa.Column(
            "order_id", sqlalchemy_utils.types.uuid.UUIDType(), nullable=True
        ),
    )
    op.create_foreign_key(None, "pizza", "order", ["order_id"], ["id"])
    op.add_column(
        "topping",
        sa.Column(
            "order_id", sqlalchemy_utils.types.uuid.UUIDType(), nullable=True
        ),
    )
    op.create_foreign_key(None, "topping", "pizza", ["pizza_id"], ["id"])
    op.create_foreign_key(None, "topping", "order", ["order_id"], ["id"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "topping", type_="foreignkey")
    op.drop_constraint(None, "topping", type_="foreignkey")
    op.drop_column("topping", "order_id")
    op.drop_constraint(None, "pizza", type_="foreignkey")
    op.drop_column("pizza", "order_id")
    op.drop_column("order_event", "customer_id")
    # ### end Alembic commands ###