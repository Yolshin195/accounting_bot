from sqlalchemy import select

from accounting_bot.entity import UserEntity
from accounting_bot.repository.base_repository import BaseRepository


class UserRepository(BaseRepository):
    model: UserEntity = UserEntity

    async def find_by_telegram_id(self, telegram_id: int) -> UserEntity:
        find_by_telegram_id_sql = select(self.model).where(self.model.telegram_id == telegram_id)
        return await self.session.scalar(find_by_telegram_id_sql)

    async def get_or_create(self, telegram_id: int, username: str):
        user = await self.find_by_telegram_id(telegram_id)
        if user is None:
            user = await self.add_one(UserEntity(telegram_id=telegram_id, username=username, created_by="system"))
        return user
