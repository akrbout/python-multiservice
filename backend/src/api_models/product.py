from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int = Field()
    name: str = Field()
    price: float = Field()
    image_url: str = Field(alias="imageUrl")
    description: str = Field()
