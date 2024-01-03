from sqlalchemy.ext.asyncio import AsyncSession
from src.storage.models import Order
from sqlalchemy import func, select, Select


class OrderCrud:
    session: AsyncSession

    def __init__(self, session: AsyncSession):
        self.session = session

    async def _execute_statement_for_one(self, statement: Select):
        results = await self.session.execute(statement)
        return results.unique().scalar_one_or_none()

    async def _execute_statement_for_list(self, statement: Select):
        results = await self.session.execute(statement)
        return results.all()

    async def get_product(self, id: int):
        statement = select(Product).where(Product.id == id)
        return await self._execute_statement_for_one(statement)

    async def get_products_list(self):
        statement = select(Product)
        return await self._execute_statement_for_list(statement)

    async def create_product(self, product: Product):
        self.session.add(product)
        await self.session.commit()
        await self.session.refresh(product)
        return product
