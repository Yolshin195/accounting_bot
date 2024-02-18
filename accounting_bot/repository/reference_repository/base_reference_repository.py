from sqlalchemy import select

from accounting_bot.repository.base_repository import BaseRepository, ModelType


class BaseReferenceRepository(BaseRepository):

    async def find_by_code(self, code: str) -> ModelType:
        find_by_code = select(self.model).where(self.model.code == code)
        return await self.session.scalar(find_by_code)
