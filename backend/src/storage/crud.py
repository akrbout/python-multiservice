from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Select


class BaseCrud:
    session: AsyncSession

    def __init__(self, session: AsyncSession):
        self.session = session

    async def _execute_statement_for_one(self, statement: Select):
        results = await self.session.execute(statement)
        return results.unique().scalar_one_or_none()

    async def _execute_statement_for_list(self, statement: Select):
        results = await self.session.execute(statement)
        return results.all()
