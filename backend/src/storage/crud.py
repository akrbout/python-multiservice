from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Select, select


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

    async def get_first_one(self, id: int, obj: ...):
        statement = select(obj).where((obj.id == id) and (obj.is_deleted is not True))
        return await self._execute_statement_for_one(statement)

    async def get_all(self, obj: ...):
        statement = select(obj).where(obj.is_deleted is not True)
        return await self._execute_statement_for_list(statement)

    async def create(self, obj: ...):
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    async def update(self, new_obj: ...) -> bool:
        old_obj = self.get_first_one(new_obj.id, new_obj)
        if not old_obj:
            return False
        res = await self.create(new_obj)
        return True if res else False

    async def delete(self, obj: ...):
        if not obj.is_deleted:
            obj.is_deleted = True
        return await self.update(obj)
