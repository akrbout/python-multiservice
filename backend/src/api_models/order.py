import enum
from datetime import datetime

from pydantic import BaseModel, Field

from src.api_models.product import Product


class OrderStatus(enum.Enum):
    created = "created"
    pending = "pending"
    transit = "transit"
    received = "received"
    completed = "completed"


class Order(BaseModel):
    id: int = Field()
    created_dttm: datetime = Field(default_factory=datetime.now)
    products: list[Product] = Field()
    description: str = Field()
    status: OrderStatus = Field()
    total_price: int = Field()
    total_discount: int = Field()
