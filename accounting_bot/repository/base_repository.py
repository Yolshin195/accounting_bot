from typing import Type, TypeVar, Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from accounting_bot.entity import BaseEntity

# Объявляем тип-параметр ModelType, который будет использоваться для моделей
ModelType = TypeVar('ModelType', bound=BaseEntity)


class BaseRepository:
    model: Type[ModelType] = NotImplementedError

    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def find_all(self, skip: int = 0, limit: int = 100) -> Sequence[ModelType]:
        find_all_sql = select(self.model).offset(skip).limit(limit)
        result = await self.session.scalars(find_all_sql)
        return result.all()

    async def find_by_id(self, model_id: UUID) -> ModelType:
        find_by_id = select(self.model).where(self.model.id == model_id)
        return await self.session.scalar(find_by_id)

    async def add_one(self, model: ModelType) -> ModelType:
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)
        return model
