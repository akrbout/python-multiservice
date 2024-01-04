from datetime import datetime

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import String, ARRAY, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    created_on: Mapped[datetime] = mapped_column(default=datetime.now())
    updated_on: Mapped[datetime] = mapped_column(default=datetime.now())


class Product(Base):
    name: Mapped[str]
    price: Mapped[int]
    image_url: Mapped[str]
    description: Mapped[str]
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    warehouse_positions = relationship("WarehousePosition")
    order_details = relationship("OrderDetail")

    __tablename__ = "product"


class Review(Base):
    author: Mapped[str]
    rate: Mapped[float | None]
    review_desc: Mapped[str]
    source_url: Mapped[str]
    product_id: Mapped[str] = mapped_column(ForeignKey("product.id"))

    __tablename__ = "review"


class OrderDetail(Base):
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
    ordered_count: Mapped[int]

    __tablename__ = "order_detail"


class Order(Base):
    description_desc: Mapped[str | None]
    status: Mapped[str]
    total_price: Mapped[int]
    total_discount: Mapped[int] = mapped_column(default=0)
    source_warehouse: Mapped[int]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    order_details = relationship("OrderDetail")
    delivery_status_id: Mapped[int] = mapped_column(ForeignKey("delivery_status.id"))

    __tablename__ = "order"


class Category(Base):
    name: Mapped[str]
    description_desc: Mapped[str]
    products = relationship("Product")

    __tablename__ = "category"


class Warehouse(Base):
    address: Mapped[str]
    manager_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    __tablename__ = "warehouse"


class WarehousePosition(Base):
    warehouse: Mapped[int] = mapped_column(ForeignKey("warehouse.id"))
    unic: Mapped[str] = mapped_column(unique=True)
    count: Mapped[int]
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))

    __tablename__ = "warehouse_position"


class DeliveryStatus(Base):
    name: Mapped[str]
    description_desc: Mapped[str]
    orders = relationship("Order")

    __tablename__ = "delivery_status"


class User(SQLAlchemyBaseUserTable[int], Base):
    full_nm: Mapped[str | None]
    phone_num: Mapped[str | None]
    role: Mapped[str | None]
    photo_base64: Mapped[str | None]
    username: Mapped[str | None]
    warehouses = relationship("Warehouse")
    orders = relationship("Order")

    __tablename__ = "user"
