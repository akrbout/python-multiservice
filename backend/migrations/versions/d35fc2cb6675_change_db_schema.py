"""Change DB schema

Revision ID: d35fc2cb6675
Revises: d6c048de272a
Create Date: 2024-01-04 01:31:08.882124

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd35fc2cb6675'
down_revision: Union[str, None] = 'd6c048de272a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order_detail',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('ordered_count', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('updated_on', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('delivery_status', 'source_warehouse')
    op.add_column('order', sa.Column('description_desc', sa.String(), nullable=True))
    op.add_column('order', sa.Column('user_id', sa.Integer(), nullable=False))
    op.add_column('order', sa.Column('delivery_status_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'order', 'delivery_status', ['delivery_status_id'], ['id'])
    op.create_foreign_key(None, 'order', 'user', ['user_id'], ['id'])
    op.drop_column('order', 'description')
    op.drop_column('order', 'products')
    op.add_column('product', sa.Column('category_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'product', 'category', ['category_id'], ['id'])
    op.drop_column('product', 'warehouses')
    op.drop_column('product', 'category')
    op.add_column('review', sa.Column('source_url', sa.String(), nullable=False))
    op.add_column('review', sa.Column('product_id', sa.Integer(), nullable=False))
    op.alter_column('review', 'rate',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               nullable=True)
    op.create_foreign_key(None, 'review', 'product', ['product_id'], ['id'])
    op.drop_column('review', 'product')
    op.add_column('warehouse', sa.Column('manager_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'warehouse', 'user', ['manager_id'], ['id'])
    op.drop_column('warehouse', 'manager')
    op.add_column('warehouse_position', sa.Column('unic', sa.String(), nullable=False))
    op.add_column('warehouse_position', sa.Column('product_id', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'warehouse_position', ['unic'])
    op.create_foreign_key(None, 'warehouse_position', 'product', ['product_id'], ['id'])
    op.create_foreign_key(None, 'warehouse_position', 'warehouse', ['warehouse'], ['id'])
    op.drop_column('warehouse_position', 'product')
    op.drop_column('warehouse_position', 'unic_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('warehouse_position', sa.Column('unic_id', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('warehouse_position', sa.Column('product', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'warehouse_position', type_='foreignkey')
    op.drop_constraint(None, 'warehouse_position', type_='foreignkey')
    op.drop_constraint(None, 'warehouse_position', type_='unique')
    op.drop_column('warehouse_position', 'product_id')
    op.drop_column('warehouse_position', 'unic')
    op.add_column('warehouse', sa.Column('manager', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'warehouse', type_='foreignkey')
    op.drop_column('warehouse', 'manager_id')
    op.add_column('review', sa.Column('product', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'review', type_='foreignkey')
    op.alter_column('review', 'rate',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               nullable=False)
    op.drop_column('review', 'product_id')
    op.drop_column('review', 'source_url')
    op.add_column('product', sa.Column('category', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('product', sa.Column('warehouses', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'product', type_='foreignkey')
    op.drop_column('product', 'category_id')
    op.add_column('order', sa.Column('products', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=False))
    op.add_column('order', sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'order', type_='foreignkey')
    op.drop_constraint(None, 'order', type_='foreignkey')
    op.drop_column('order', 'delivery_status_id')
    op.drop_column('order', 'user_id')
    op.drop_column('order', 'description_desc')
    op.add_column('delivery_status', sa.Column('source_warehouse', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_table('order_detail')
    # ### end Alembic commands ###
