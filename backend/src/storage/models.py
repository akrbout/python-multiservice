from datetime import datetime

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import String, ARRAY
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    created_on: Mapped[datetime] = mapped_column(default=datetime.now())
    updated_on: Mapped[datetime] = mapped_column(default=datetime.now())


class Product(Base):
    name: Mapped[str]
    price: Mapped[int]
    image_url: Mapped[str]
    description: Mapped[str]
    category: Mapped[int]
    warehouse: Mapped[int]
    total_count: Mapped[int]

    __tablename__ = "product"


class Review(Base):
    author: Mapped[str]
    product: Mapped[str]
    rate: Mapped[int]
    review_desc: Mapped[str]

    __tablename__ = "review"


class Order(Base):
    products: Mapped[list[str]] = mapped_column(ARRAY(String))
    description: Mapped[str | None]
    status: Mapped[str]
    total_price: Mapped[int]
    total_discount: Mapped[int] = mapped_column(default=0)

    __tablename__ = "order"


class Category(Base):
    name: Mapped[str]
    description_desc: Mapped[str]

    __tablename__ = "category"


class Warehouse(Base):
    address: Mapped[str]
    manager: Mapped[int]

    __tablename__ = "warehouse"


class User(SQLAlchemyBaseUserTable[int], Base):
    full_name: Mapped[str | None]
    phone_num: Mapped[str | None]
    role: Mapped[str | None]
    photo_url: Mapped[str | None]
    username: Mapped[str | None]

    __tablename__ = "user"
